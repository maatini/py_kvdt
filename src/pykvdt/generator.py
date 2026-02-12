import random
import string
from datetime import datetime, timedelta
from typing import List, Union, Optional
from .model import Satz, Token, FieldReference, GroupReference
from .definitions import FIELDS, DATUM, GOP, ZEITRAUM, ALPHANUMERISCH, NUMERISCH
from .structures import SENTENCE_TYPES

from .generator_context import GeneratorContext

class Generator:
    def __init__(self, context: Optional[GeneratorContext] = None):
        self.sentence_type = ""
        self.context = context or GeneratorContext()

    def generate_kvdt_file(self, min_cases: int = 5, max_cases: int = 10) -> List[Satz]:
        """
        Generates a full KVDT file structure (Arztpakete).
        Sequence: con0 -> besa -> adt0 -> cases -> adt9 -> con9
        """
        sentences = []
        
        # 1. Container Header
        sentences.append(self.generate_sentence("con0"))
        
        # 2. Betriebsstättendaten (besa)
        # BSNR/LANR are already in context, but besa defines them in the file.
        # We need to ensure the generated besa matches our context.
        # For now, generate_sentence uses context for fields, so it should match.
        sentences.append(self.generate_sentence("besa"))
        
        # 3. ADT Packet Header
        sentences.append(self.generate_sentence("adt0"))
        
        # 4. Cases (Arztpakete content)
        # Generate a random number of cases
        num_cases = random.randint(min_cases, max_cases)
        case_types = ["0101", "0102", "0103", "0104"]
        
        for _ in range(num_cases):
            # Sort cases by date? The requirement says chronologically.
            # For random generation, we can just generate them. 
            # If strict sorting is needed, we would need to post-process 
            # or force dates to be increasing.
            # For now, random mix.
            satz_type = random.choice(case_types)
            sentences.append(self.generate_sentence(satz_type))
            
        # 5. ADT Packet Footer
        sentences.append(self.generate_sentence("adt9"))
        
        # 6. Container Footer
        sentences.append(self.generate_sentence("con9"))
        
        return sentences


    def generate_sentence(self, satzart_id: str) -> Satz:
        """
        Generates a valid Satz object with random data for the given sentence type ID.
        """
        if satzart_id not in SENTENCE_TYPES:
            raise ValueError(f"Unknown sentence type: {satzart_id}")
        
        definition = SENTENCE_TYPES[satzart_id]
        self.sentence_type = satzart_id
        tokens = []
        
        # Determine strict structure generation
        self._generate_structure(definition.structure, tokens)
        
        return Satz(type=satzart_id, tokens=tokens)

    def _generate_structure(self, structure: List[Union[FieldReference, GroupReference]], tokens: List[Token]):
        for item in structure:
            if isinstance(item, FieldReference):
                self._generate_field(item, tokens)
            elif isinstance(item, GroupReference):
                self._generate_group(item, tokens)

    def _generate_field(self, field_ref: FieldReference, tokens: List[Token]):
        # Determine repetition count
        count = 1
        if field_ref.count == -1:
            # Random repetition for unlimited fields (1 to 3 times)
            count = random.randint(1, 3) 
        elif field_ref.count > 1:
            count = field_ref.count
            
        # Handle mandatory/optional
        if not field_ref.mandatory:
            # Check rules first. If disallowed by rule, skip it.
            if not self._check_rules(field_ref.rules):
                return
            
            # 50% chance to skip optional field if not mandatory
            if random.choice([True, False]):
                return

        for _ in range(count):
            content = self._generate_content(field_ref.field_id)
            tokens.append(Token(type=field_ref.field_id, attr=content, line_nbr=1))

    def _generate_group(self, group_ref: GroupReference, tokens: List[Token]):
        # Determine repetition count
        count = 1
        if group_ref.count == -1:
             # Random repetition for unlimited groups
            count = random.randint(1, 3)
        elif group_ref.count > 1:
            count = group_ref.count

        # Handle mandatory/optional
        if not group_ref.mandatory:
             # Check rules first. If disallowed by rule, skip it.
            if not self._check_rules(group_ref.rules):
                return
                
            # 50% chance to skip optional group
            if random.choice([True, False]):
                return

        for _ in range(count):
            self._generate_structure(group_ref.items, tokens)

    def _generate_content(self, field_id: str) -> str:
        if field_id not in FIELDS:
            # Fallback for unknown fields
            return "TEST"
            
        # Context-aware generation
        if field_id == "8000":
            return self.sentence_type
        if field_id in ["0201", "0217", "0218"]: # BSNR fields
            return self.context.bsnr
        if field_id in ["0212", "4241", "4242", "5099"]: # LANR fields
            return self.context.get_random_lanr()
            
        # Realistic data mapping
        if field_id == "3101": # Nachname
            return self.context.get_last_name()
        if field_id == "3102": # Vorname
            return self.context.get_first_name()
        if field_id == "3107": # Strasse
            return self.context.get_street()
        if field_id == "3112": # PLZ
            return self.context.get_city_data()[0]
        if field_id == "3113": # Ort
            return self.context.get_city_data()[1]
        if field_id == "5001": # GOP
            return self.context.get_gop()
        if field_id in ["6001", "3673"]: # ICD-Kode (3-byte version)
            return self.context.get_icd_3()
        if field_id == "6003": # Diagnosensicherheit
            return self.context.get_diagnose_certainty()
        if field_id == "3119": # Versichertennummer eGK
            return self.context.get_insurance_id()
        if field_id == "4112": # Versichertenstatus
            return self.context.get_insurance_status()
        if field_id == "4101": # Quartal
            return self.context.get_quarter()
        if field_id == "4106": # KTAB
            return self.context.get_ktab()
        field_def = FIELDS[field_id]
        # Calculate length to generate
        length = field_def.max_len
        if length == 0: length = 10 # Default for variable length
        
        # Override for specific types or strict length requirements
        if field_def.min_len > 0 and field_def.min_len == field_def.max_len:
            length = field_def.max_len
        elif field_def.max_len > 0:
             length = random.randint(field_def.min_len, field_def.max_len)
        
        if field_def.type == DATUM:
            return self._random_date()
        elif field_def.type == ZEITRAUM:
             # Format YYYYMMDDYYYYMMDD
            d1 = self._random_date_obj()
            d2 = d1 + timedelta(days=random.randint(1, 30))
            return d1.strftime("%d%m%Y") + d2.strftime("%d%m%Y")
        elif field_def.type == NUMERISCH:
            return self._random_numeric(length)
        elif field_def.type == GOP:
             return self._random_numeric(length) # GOP is mostly numeric
        else:
            return self._random_alphanumeric(length)

    def _random_date(self) -> str:
        d = self._random_date_obj()
        return d.strftime("%d%m%Y")

    def _random_date_obj(self) -> datetime:
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2025, 12, 31)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        return start_date + timedelta(days=random_number_of_days)

    def _random_numeric(self, length: int) -> str:
        # returns string of digits
        if length <= 0: return "0"
        return ''.join(random.choices(string.digits, k=length))

    def _random_alphanumeric(self, length: int) -> str:
        # returns string of chars
        if length <= 0: return ""
        # Avoid special chars for now to be safe
        chars = string.ascii_letters + string.digits + " "
        return ''.join(random.choices(chars, k=length))

    def _check_rules(self, rules: List[str]) -> bool:
        """
        Checks if the rules allow generation. 
        Returns True if allowed (or no rules), False if forbidden.
        """
        if not rules:
            return True
            
        context = {"Satzart": self.sentence_type}
        
        for rule in rules:
             # Handle Lambda Rules (Context checks)
            if rule.strip().startswith("(lambda") or rule.strip().startswith("lambda"):
                try:
                    rule_expr = rule if rule.strip().startswith("(") else f"({rule})"
                    # Eval to get the function - same as Parser
                    rule_func = eval(rule_expr, {"__builtins__": {}}, {})
                    if not rule_func(context):
                        return False
                except Exception:
                    # If evaluation fails, we assume allowed for generator to proceed, 
                    # or disallowed? Safest is to allow and let validation catch it,
                    # but here we want to avoid generating disallowed optional stuff.
                    # If we don't know, maybe we ignore rule.
                    pass
        return True
