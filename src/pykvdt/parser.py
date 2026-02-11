from typing import List, Iterator, Dict, Any, Union, Optional
from .model import Satz, Token, FieldReference, GroupReference, ValidationResult
from .definitions import FIELDS
from .structures import SENTENCE_TYPES
from .validators import Validator

class Parser:
    def __init__(self):
        pass

    def validate_sentence(self, satz: Satz) -> ValidationResult:
        if satz.type not in SENTENCE_TYPES:
             return ValidationResult(False, [f"Unknown sentence type: {satz.type}"])
        
        self.current_satz_type = satz.type
        definition = SENTENCE_TYPES[satz.type]
        self.errors: List[str] = []
        self.tokens = satz.tokens
        self.pos = 0
        
        # Start matching the top-level structure
        self._match_structure(definition.structure)
        
        # Check for excess tokens
        if self.pos < len(self.tokens):
             self.errors.append(f"Excess tokens starting at index {self.pos}: {self.tokens[self.pos].type}")

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
            self.errors.append(f"Missing mandatory field {field_ref.field_id}")

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
             # It's mandatory but we didn't find it even once.
             # However, determining "missing group" is hard without a clear start marker.
             # If _group_starts_here returned False, maybe it's missing?
             # For now we report it, but this might need refinement for complex optional groups.
             self.errors.append(f"Missing mandatory group starting with {self._get_group_start_id(group_ref)}")

    def _group_starts_here(self, group_ref: GroupReference) -> bool:
        """
        Recursively checks if the current token matches the start of the group.
        """
        token = self._current_token()
        if not token:
            return False
            
        first_item = group_ref.items[0] if group_ref.items else None
        if not first_item:
            return False # Empty group?

        if isinstance(first_item, FieldReference):
            return token.type == first_item.field_id
        elif isinstance(first_item, GroupReference):
            return self._group_starts_here(first_item)
        
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
            self.errors.append(f"Unknown field definition for {token.type}")
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
             self.errors.append(f"Field {token.type} content invalid: '{token.attr}' (Expected type: {field_def.type})")
        else:
             # Length Validation (only if content format is valid)
             l = len(token.attr)
             if field_def.max_len > 0: # 0 means unlimited/unknown in my migration script fallback
                if l < field_def.min_len or l > field_def.max_len:
                    self.errors.append(f"Field {token.type} length mismatch: got {l}, expected {field_def.min_len}-{field_def.max_len}")
        
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
                     self.errors.append(f"Rule failed for {token.type}: {rule}")

            except Exception as e:
                self.errors.append(f"Error evaluating rule '{rule}' for {token.type}: {e}")
        
        else:
            # Semantic Rules (e.g. "R743")
            # These require specific implementation of business logic.
            # For now we acknowledge them.
            pass
