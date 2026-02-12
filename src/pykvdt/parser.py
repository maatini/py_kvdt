from typing import List, Iterator, Dict, Any, Union, Optional
from .model import Satz, Token, FieldReference, GroupReference, ValidationResult, ValidationErrorObject
from .definitions import FIELDS
from .structures import SENTENCE_TYPES
from .validators import Validator

class Parser:
    def __init__(self):
        pass

    def validate_sentence(self, satz: Satz) -> ValidationResult:
        if satz.type not in SENTENCE_TYPES:
             return ValidationResult(False, [ValidationErrorObject(f"Unknown sentence type: {satz.type}", satz_type=satz.type)])
        
        self.current_satz_type = satz.type
        definition = SENTENCE_TYPES[satz.type]
        self.errors: List[ValidationErrorObject] = []
        self.tokens = satz.tokens
        self.pos = 0
        
        # Start matching the top-level structure
        self._match_structure(definition.structure)
        
        # Check for excess tokens
        if self.pos < len(self.tokens):
             token = self.tokens[self.pos]
             self.errors.append(ValidationErrorObject(
                 f"Excess tokens starting with {token.type}", 
                 field_id=token.type, 
                 line_nbr=token.line_nbr, 
                 satz_type=self.current_satz_type
             ))

        return ValidationResult(len(self.errors) == 0, self.errors)

    def _current_token(self) -> Optional[Token]:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _advance(self):
        self.pos += 1

    def _match_structure(self, structure: List[Union[FieldReference, GroupReference]]):
        for item in structure:
            if isinstance(item, FieldReference):
                self._match_field(item)
            elif isinstance(item, GroupReference):
                self._match_group(item)

    def _match_field(self, field_ref: FieldReference):
        count = 0
        while True:
            token = self._current_token()
            if token and token.type == field_ref.field_id:
                self._validate_token_content(token, field_ref)
                self._advance()
                count += 1
                
                # If we reached max count (and max count is not infinite -1)
                if field_ref.count != -1 and count >= field_ref.count:
                    break
            else:
                # Token doesn't match field_id
                break
        
        if field_ref.mandatory and count == 0:
            last_token = self.tokens[self.pos-1] if self.pos > 0 else None
            line_nbr = last_token.line_nbr if last_token else None
            self.errors.append(ValidationErrorObject(
                f"Missing mandatory field {field_ref.field_id}", 
                field_id=field_ref.field_id,
                line_nbr=line_nbr,
                satz_type=self.current_satz_type
            ))

    def _match_group(self, group_ref: GroupReference):
        # Groups are complex because they don't have a single Token ID to peek at.
        # We need to know if the group starts here.
        # A group starts if the FIRST item in the group matches.
        # This is a simplification; KVDT groups usually start with a specific field.
        
        count = 0
        while True:
            # Check if group starts here
            if not self._group_starts_here(group_ref):
                break

            # Consume group
            self._match_structure(group_ref.items)
            count += 1
            
            if group_ref.count != -1 and count >= group_ref.count:
                break
        
        if group_ref.mandatory and count == 0:
             start_id = self._get_group_start_id(group_ref)
             last_token = self.tokens[self.pos-1] if self.pos > 0 else None
             line_nbr = last_token.line_nbr if last_token else None
             self.errors.append(ValidationErrorObject(
                 f"Missing mandatory group starting with {start_id}", 
                 field_id=start_id,
                 line_nbr=line_nbr,
                 satz_type=self.current_satz_type
             ))

    def _group_starts_here(self, group_ref: GroupReference) -> bool:
        """
        Recursively checks if the current token matches the start of the group.
        Handles optional leading items by checking subsequent items.
        """
        token = self._current_token()
        if not token:
            return False
            
        for item in group_ref.items:
            match = False
            if isinstance(item, FieldReference):
                match = (token.type == item.field_id)
            elif isinstance(item, GroupReference):
                match = self._group_starts_here(item)
            
            if match:
                return True
            
            # If the item is mandatory, and we didn't match it, then the group definitely doesn't start here.
            # (Because if the group started here, this mandatory item MUST be present or be the start).
            # Wait, if item is mandatory, it MUST be the first thing if previous were missing?
            # Yes. If we haven't found a match yet, and we hit a mandatory item, 
            # then that mandatory item IS the expected start. If it doesn't match, the group isn't here.
            if item.mandatory:
                return False
                
            # If item is optional, we continue to the next item to see if IT starts the group.
            
        return False

    def _get_group_start_id(self, group_ref: GroupReference) -> str:
        if not group_ref.items: return "?"
        item = group_ref.items[0]
        if isinstance(item, FieldReference): return item.field_id
        if isinstance(item, GroupReference): return self._get_group_start_id(item)
        return "?"

    def _validate_token_content(self, token: Token, field_ref: FieldReference):
        field_def = FIELDS.get(token.type)
        if not field_def:
            self.errors.append(ValidationErrorObject(
                f"Unknown field definition for {token.type}", 
                field_id=token.type,
                line_nbr=token.line_nbr,
                satz_type=self.current_satz_type
            ))
            return

        valid_content = True
        # Basic Type Validation
        if field_def.type == 'd':
            valid_content = Validator.check_date(token.attr)
        elif field_def.type == 'n':
            valid_content = Validator.check_numeric(token.attr)
        elif field_def.type == 'z':
            valid_content = Validator.check_period(token.attr)
        elif field_def.type == 'g':
            valid_content = Validator.check_gop(token.attr)
        
        if not valid_content:
             self.errors.append(ValidationErrorObject(
                 f"Content invalid: '{token.attr}' (Expected type: {field_def.type})",
                 field_id=token.type,
                 line_nbr=token.line_nbr,
                 satz_type=self.current_satz_type
             ))
        else:
             # Length Validation (only if content format is valid)
             l = len(token.attr)
             if field_def.max_len > 0: # 0 means unlimited/unknown in my migration script fallback
                if l < field_def.min_len or l > field_def.max_len:
                    self.errors.append(ValidationErrorObject(
                        f"Length mismatch: got {l}, expected {field_def.min_len}-{field_def.max_len}",
                        field_id=token.type,
                        line_nbr=token.line_nbr,
                        satz_type=self.current_satz_type
                    ))
        
        # Rule Validation (Placeholder)
        if field_ref.rules:
            for rule in field_ref.rules:
                self._check_rule(rule, token)

    def _check_rule(self, rule: str, token: Token):
        # Handle Lambda Rules (Context checks)
        if rule.strip().startswith("(lambda") or rule.strip().startswith("lambda"):
            try:
                # Prepare safe context
                # Legacy code expected 'kontext' dict with 'Satzart'
                # We can construct a minimal context. 
                # Note: Real validation might need more context (previous fields etc), 
                # but currently we only have 'Satzart' from the Sentence definition.
                # In the future, we should build a full context object.
                
                # For safety, avoid eval if possible, but for migration it's the only way to support legacy lambdas.
                # We compile the lambda and call it.
                
                # Wrap in parens if not already to ensure it evaluates to a callable
                rule_expr = rule if rule.strip().startswith("(") else f"({rule})"
                
                # Eval to get the function
                rule_func = eval(rule_expr, {"__builtins__": {}}, {})
                
                # Call it
                # We need the Satzart. We stored it in self.satz_type? No.
                # We need to access the sentence type being parsed.
                # Let's store it in __init__ or validate_sentence
                
                context = {"Satzart": self.current_satz_type}
                if not rule_func(context):
                     self.errors.append(ValidationErrorObject(
                         f"Rule failed: {rule}",
                         field_id=token.type,
                         line_nbr=token.line_nbr,
                         satz_type=self.current_satz_type
                     ))

            except Exception as e:
                self.errors.append(ValidationErrorObject(
                    f"Error evaluating rule '{rule}': {e}",
                    field_id=token.type,
                    line_nbr=token.line_nbr,
                    satz_type=self.current_satz_type
                ))
        
        else:
            # Semantic Rules (e.g. "R743")
            # These require specific implementation of business logic.
            # For now we acknowledge them.
            pass
