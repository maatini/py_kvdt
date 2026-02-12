import re

# Read legacy file content directly since we can't import easily from legacy folder structure
with open('legacy/kvdt_feld_stm.py', 'r', encoding='iso-8859-15') as f:
    content = f.read()

# Regex to find dictionary entries: 'XXXX': ["Description", [min, max, TYPE]]
# Example: '0102': ["Softwareverantwortlicher (SV) ...", [0, 60, ALPHANUMERISCH]],
pattern = re.compile(r"'(\d{4})':\s*\[\"(.*?)\",\s*\[(.*?)\]\],?")

matches = pattern.findall(content)

print("from .model import FieldDefinition")
print("")
print("# Field Types")
print("DATUM = 'd'")
print("GOP = 'g'")
print("ZEITRAUM = 'z'")
print("ALPHANUMERISCH = 'a'")
print("NUMERISCH = 'n'")
print("")
print("FIELDS = {")

for fk, desc, type_info in matches:
    # Clean up description (remove English translation after /)
    desc_clean = desc.split("/")[0].strip()

    # Parse type info: 0, 60, ALPHANUMERISCH
    parts = [p.strip() for p in type_info.split(",")]

    if len(parts) >= 3:
        min_len = parts[0]
        max_len = parts[1]
        field_type = parts[-1]
    elif len(parts) == 1:
        # Special types like [DATUM] which maps to 'd' in legacy code variable
        if parts[0] == 'DATUM':
            min_len = 8
            max_len = 8
            field_type = 'DATUM'
        elif parts[0] == 'ZEITRAUM':
            min_len = 16
            max_len = 16
            field_type = 'ZEITRAUM'
        else:
            # Fallback
            min_len = 0
            max_len = 0
            field_type = "'?'"
    else:
        min_len = 0
        max_len = 0
        field_type = "'?'"

    print(
        f"    '{fk}': FieldDefinition('{fk}', \"{desc_clean}\", "
        f"{min_len}, {max_len}, {field_type}),"
    )

print("}")
