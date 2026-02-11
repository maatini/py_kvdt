from typing import List, Iterator, Dict, Any, Union
from .model import Satz, Token, FieldReference, GroupReference
from .definitions import FIELDS
from .structures import SENTENCES
from .validators import Validator

class ValidationResult:
    def __init__(self, valid: bool, errors: List[str]):
        self.valid = valid
        self.errors = errors

class Parser:
    def __init__(self):
        pass

    def validate_sentence(self, satz: Satz) -> ValidationResult:
        definition = SENTENCES.get(satz.type)
        if not definition:
             # Unknown sentence type, maybe just ignore or warn?
             return ValidationResult(False, [f"Unknown sentence type: {satz.type}"])
        
        errors = []
        token_iter = iter(satz.tokens)
        current_token = next(token_iter, None)

        # Helper to consume tokens
        def advance():
            nonlocal current_token
            current_token = next(token_iter, None)

        def match_structure(structure: List[Union[FieldReference, GroupReference]]) -> bool:
            nonlocal current_token
            # This is a simplified recursive descent. 
            # In a full implementation, we need backtracking or lookahead for optional complex groups.
            # strict KVDT is usually deterministic enough.
            
            for item in structure:
                if isinstance(item, FieldReference):
                    # Check if current token matches field_id
                    # Handle repetition
                    count = 0
                    while current_token and current_token.type == item.field_id:
                        # Validate Content
                        field_def = FIELDS.get(item.field_id)
                        if field_def:
                            valid_content = True
                            if field_def.type == 'd':
                                valid_content = Validator.check_date(current_token.attr)
                            elif field_def.type == 'n':
                                valid_content = Validator.check_numeric(current_token.attr)
                            elif field_def.type == 'z':
                                valid_content = Validator.check_period(current_token.attr)
                            elif field_def.type == 'g':
                                valid_content = Validator.check_gop(current_token.attr)
                            
                            # Check length
                            if valid_content: # Only check length if format validation didn't fail already (for strict types)
                                l = len(current_token.attr)
                                if l < field_def.min_len or l > field_def.max_len:
                                    errors.append(f"Field {item.field_id} length mismatch: got {l}, expected {field_def.min_len}-{field_def.max_len}")
                            
                            if not valid_content:
                                errors.append(f"Field {item.field_id} content invalid: {current_token.attr} (Type: {field_def.type})")
                        
                        count += 1
                        advance()
                        if item.count != -1 and count >= item.count:
                            break
                    
                    if item.mandatory and count == 0:
                        errors.append(f"Missing mandatory field {item.field_id}")
                
                elif isinstance(item, GroupReference):
                    # Groups are trickier, usually just lists of fields in KVDT
                    # We recurse
                    # Handle repetition of the GROUP
                    count = 0
                    while True:
                         # We need to peek if the group starts here.
                         # This requires lookahead which this simple iterator doesn't support well.
                         # For this refactoring, I will simplify and assume no complex group repetition for now
                         # or just implement single pass.
                         match_structure(item.items)
                         count += 1
                         if item.count != -1 and count >= item.count:
                             break
                         # If optional and no match, break (needs lookahead)
                         break 

            return True

        match_structure(definition.structure)
        
        if current_token is not None:
             errors.append(f"Excess tokens starting at {current_token.type}")

        return ValidationResult(len(errors) == 0, errors)
