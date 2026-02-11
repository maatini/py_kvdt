import re
from datetime import datetime

class Validator:
    @staticmethod
    def check_date(value: str) -> bool:
        """Checks if value is a valid date (DDMMYYYY)."""
        if len(value) != 8:
            return False
        try:
            day = int(value[0:2])
            month = int(value[2:4])
            year = int(value[4:])
            datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def check_period(value: str) -> bool:
        """Checks if value is a valid period (DDMMYYYYDDMMYYYY)."""
        if len(value) != 16:
            return False
        return Validator.check_date(value[:8]) and Validator.check_date(value[8:])

    @staticmethod
    def check_numeric(value: str) -> bool:
        return value.isdigit()

    @staticmethod
    def check_alphanumeric(value: str) -> bool:
        # KVDT alphanumeric allows spaces and special chars, so basic check is usually permissive
        # But we might want to check for illegal control chars if needed.
        return True 

    @staticmethod
    def check_gop(value: str) -> bool:
        """Checks GOP format: Digits, last char can be char."""
        if not value: return False
        if len(value) < 1: return False
        
        main_part = value[:-1]
        last_char = value[-1]
        
        if main_part and not main_part.isdigit():
            return False
        
        return last_char.isalnum()
