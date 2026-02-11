import ast
import re

# Read legacy file
with open('legacy/kvdt_satzarten.py', 'r', encoding='iso-8859-15') as f:
    content = f.read()

# Filter out imports and comments to make it parseable as AST or just use regex/parsing logic
# Since the file is Python, we can try to use ast.parse, but it imports 'kvdt_process' and others which we don't want to load.
# So we will parse the AST of the file without executing it.

tree = ast.parse(content)

structures = {}

def parse_element(el):
    """
    Parses a list element from the AST.
    Structure: [FK, NAME, COUNT, MANDATORY, RULES, SUBSTRUCTURES, (ProcessFunc)?]
    """
    # Special case: Flat list 'Leistungen' has structure ["FK", "Name", Count, Mand, Rules, Sub] directly in the list
    # Not wrapped in inner lists for the top level.
    # We need to detect if 'el' is a list (Group/Field definition) or if we are parsing a flat list.
    
    if not isinstance(el, ast.List):
        return None
    
    # Standard check: must have at least 6 elements [FK, NAME, COUNT, MAND, RULES, SUB]
    if len(el.elts) < 6:
        # print(f"# Skipping element with {len(el.elts)} items: {ast.dump(el)}")
        return None

    # 0: FK (String)
    fk_node = el.elts[0]
    fk = fk_node.s if hasattr(fk_node, 's') else fk_node.value
    
    # 2: Count (Num/Constant)
    count_node = el.elts[2]
    if isinstance(count_node, ast.UnaryOp) and isinstance(count_node.op, ast.USub):
         count = -1
    else:
         count = count_node.n if hasattr(count_node, 'n') else count_node.value

    # 3: Mandatory (String)
    m_node = el.elts[3]
    mandatory_str = m_node.s if hasattr(m_node, 's') else m_node.value
    mandatory = (mandatory_str == 'm')

    # 4: Rules (List)
    rules_node = el.elts[4]
    rules = []
    if isinstance(rules_node, ast.List):
        for r in rules_node.elts:
             if hasattr(r, 's'): rules.append(r.s)
             elif hasattr(r, 'value'): rules.append(r.value)
    
    # 5: Substructure (List)
    sub_node = el.elts[5]
    subitems = []
    if isinstance(sub_node, ast.List):
        for sub in sub_node.elts:
            parsed_sub = parse_element(sub)
            if parsed_sub:
                subitems.append(parsed_sub)
            elif isinstance(sub, ast.Name):
                 # Referenced variable (e.g., Leistungen)
                 subitems.append({'type': 'ref', 'name': sub.id})

    # If it has subitems, it's a Group, otherwise a Field
    if subitems:
        return {
            'type': 'Group',
            'items': subitems,
            'mandatory': mandatory,
            'count': count,
            'rules': rules
        }
    else:
         return {
            'type': 'Field',
            'id': fk,
            'mandatory': mandatory,
            'count': count,
            'rules': rules
        }


print("from typing import List, Union")
print("from .model import SentenceDefinition, FieldReference, GroupReference")
print("")
print("def F(id: str, mandatory: bool = True, count: int = 1, rules: List[str] = None) -> FieldReference:")
print("    return FieldReference(field_id=id, mandatory=mandatory, count=count, rules=rules or [])")
print("")
print("def G(items: List[Union[FieldReference, GroupReference]], mandatory: bool = True, count: int = 1, rules: List[str] = None) -> GroupReference:")
print("    return GroupReference(items=items, mandatory=mandatory, count=count, rules=rules or [])")
print("")

# Helper to print recursively
def print_structure(item, indent=4):
    prefix = " " * indent
    if item['type'] == 'Field':
        # Simplify defaults
        args = [f'"{item["id"]}"']
        if not item['mandatory']: args.append("mandatory=False")
        if item['count'] != 1: args.append(f"count={item['count']}")
        if item['rules']: args.append(f"rules={item['rules']}")
        return f"{prefix}F({', '.join(args)})"
    elif item['type'] == 'Group':
        lines = [f"{prefix}G(["]
        for sub in item['items']:
            if sub.get('type') == 'ref':
                 lines.append(f"{prefix}    # Reference to {sub['name']} (Handled manually or inlined if possible)")
                 # For now, we unfortunately can't verify what the ref is easily without scope analysis
                 # But usually top level definitions are 'Leistungen', 'ICD_Codes'
                 lines.append(f"{prefix}    *{sub['name']}, # Spread reference")
            else:
                 lines.append(print_structure(sub, indent + 4) + ",")
        
        lines.append(f"{prefix}], mandatory={item['mandatory']}, count={item['count']}, rules={item['rules']})")
        return "".join(line + "\n" for line in lines).strip()
    elif item['type'] == 'ref':
        return f"{prefix}*{item['name']}" # Spread

# Iterate top level assignments
for node in tree.body:
    if isinstance(node, ast.Assign):
        target_name = node.targets[0].id
        value_node = node.value
        
        # We assume top level assignments are typically definitions like s0101 = [...]
        if isinstance(value_node, ast.List):
            # Parse the list content
            # Usually the list is [ STRUCTURE_DEF ]
            # The structure definition matches parse_element
            # But wait, legacy format is: definition = [ [FK, ...], ... ] ?? 
            # Looking at file: s0101 = [ ["8000"...], ... ]
            
            # The top level list IS the structure list.
            structure_items = []
            sentence_id = target_name
            # heuristic: if '8000' is not in the first element, check if it is a flat list
            
            # Check if this is a flat definitions list (like Leistungen)
            # A flat definition list has strings/numbers directly as elements, NOT lists of lists (except for substructures)
            # e.g. Leistungen = [ "5001", "GNR", ... ]
            
            is_flat = False
            if len(value_node.elts) > 0 and isinstance(value_node.elts[0], (ast.Str, ast.Constant)):
                 is_flat = True
            
            if is_flat:
                # We need to chunk the flat list into groups of 6+ (optional func)
                # But wait, looking at 'Leistungen':
                # "5001", "GNR", -1, "m", [], [ ...sub... ], func
                # It seems to be ONE giant definition spread out? No, let's look at file.
                # It is: "5001"... then inside SUB there is a list of lists.
                # So 'Leistungen' is actually a single GROUP/FIELD definition but written flatly?
                # Actually 'Leistungen' variable seems to be used as a substructure in s0101, s0103 etc.
                # So it's effectively a reusable Group definition.
                
                # Let's verify 'Leistungen' first element
                # "5001", "GNR", -1, "m", [], [ ... ]
                # This construct looks like the content of a parse_element input, but spread into the list.
                # Let's wrap it in a list and parse it ? 
                
                # We can construct a fake List node
                fake_list = ast.List(elts=value_node.elts, ctx=ast.Load())
                parsed = parse_element(fake_list)
                if parsed:
                      structure_items.append(parsed)
            else:
                first = True
                for el in value_node.elts:
                    # If it's a name (reference)
                    if isinstance(el, ast.Name):
                        structure_items.append({'type': 'ref', 'name': el.id})
                        continue

                    parsed = parse_element(el)
                    if parsed:
                        if first and parsed['type'] == 'Field' and parsed['id'] == '8000':
                             sentence_id = parsed['id']
                             # Try to get the name from the second element if possible, but our parse_element doesn't return name
                             # We can access it from the AST node 'el' directly if we really want, but 'con0' etc matches target_name usually.
                             # For 's0101' -> 8000="0101".
                             
                             # Let's re-extract the ID from the 8000 field if possible
                             # In `s0101 = [ ["8000", "0101", ...`
                             # The second element of the list `el` is the name.
                             if len(el.elts) > 1:
                                 name_node = el.elts[1]
                                 val = name_node.s if hasattr(name_node, 's') else name_node.value
                                 if val: sentence_id = val
                                 
                        structure_items.append(parsed)
                    first = False
            
            # Generate code
            if structure_items:
                if is_flat:
                     # It's a reusable group, likely
                     print(f"{target_name} = [")
                     for item in structure_items:
                         print(f"{print_structure(item, 4)},")
                     print("]")
                     print("")
                else:
                    print(f"{target_name} = SentenceDefinition(")
                    print(f'    id="{sentence_id}",')
                    print(f'    name="{target_name}",')
                    print(f"    structure=[")
                    for item in structure_items:
                         if item.get('type') == 'ref':
                             print(f"        *{item['name']},")
                         else:
                             print(f"{print_structure(item, 8)},")
                    print("    ]")
                    print(")")
                    print("")
