import unittest
from src.pykvdt.validators import Validator

class TestValidator(unittest.TestCase):
    def test_check_date(self):
        self.assertTrue(Validator.check_date("27012024"))
        self.assertTrue(Validator.check_date("01011900"))
        self.assertFalse(Validator.check_date("32012024")) # Invalid day
        self.assertFalse(Validator.check_date("27132024")) # Invalid month
        self.assertFalse(Validator.check_date("270124"))   # Too short
        self.assertFalse(Validator.check_date("abcdefgh")) # Non-numeric

    def test_check_period(self):
        self.assertTrue(Validator.check_period("0101202431122024"))
        self.assertFalse(Validator.check_period("01012024")) # Too short
        self.assertFalse(Validator.check_period("0101202432122024")) # Invalid second date

    def test_check_numeric(self):
        self.assertTrue(Validator.check_numeric("123"))
        self.assertTrue(Validator.check_numeric("0"))
        self.assertFalse(Validator.check_numeric("12a"))
        self.assertFalse(Validator.check_numeric(""))

    def test_check_alphanumeric(self):
        self.assertTrue(Validator.check_alphanumeric("Abc 123"))
        self.assertTrue(Validator.check_alphanumeric(""))
        # Currently permissive, so everything returns True

    def test_check_gop(self):
        self.assertTrue(Validator.check_gop("01234"))
        self.assertTrue(Validator.check_gop("0123A")) # Last char letter
        self.assertTrue(Validator.check_gop("88320"))
        self.assertFalse(Validator.check_gop("01A34")) # Letter in middle
        self.assertFalse(Validator.check_gop(""))
        self.assertFalse(Validator.check_gop("A1234")) # First char letter

if __name__ == '__main__':
    unittest.main()
