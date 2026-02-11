import unittest
from src.pykvdt.parser import Parser
from src.pykvdt.model import Token, Satz

class TestParser(unittest.TestCase):
    def test_validate_sentence_valid(self):
        parser = Parser()
        # Mock a valid 'con0' sentence
        tokens = [
            Token("8000", "con0", 1),
            Token("9103", "27012024", 2), # Date valid, len 8
            Token("9132", "Datenpaket1", 3)
        ]
        satz = Satz("con0", tokens)
        
        result = parser.validate_sentence(satz)
        self.assertTrue(result.valid, f"Expected valid, got errors: {result.errors}")

    def test_validate_sentence_invalid_date_format(self):
        parser = Parser()
        tokens = [
            Token("8000", "con0", 1),
            Token("9103", "270124", 2), # Invalid date format (too short for DDMMYYYY)
            Token("9132", "Datenpaket1", 3)
        ]
        satz = Satz("con0", tokens)
        
        result = parser.validate_sentence(satz)
        self.assertFalse(result.valid)
        self.assertTrue(any("Field 9103 content invalid" in e for e in result.errors))

    def test_validate_sentence_invalid_length(self):
        parser = Parser()
        # 0201 is BSNR (len 9)
        tokens = [
            Token("8000", "besa", 1),
            Token("0201", "123", 2), # Too short (should be 9)
            Token("0203", "Praxis", 3),
            Token("0205", "Strasse", 4),
            Token("0215", "12345", 5),
            Token("0216", "Ort", 6),
            Token("0208", "012345", 7),
            Token("0211", "Arztname", 8), # Logic for mandatory group fields is tricky, lets keep simple
        ]
        # Note: BESA structure requires many fields, I will just check if 0201 length error is reported
        # even if other errors exist.
        satz = Satz("besa", tokens)
        
        result = parser.validate_sentence(satz)
        self.assertFalse(result.valid)
        self.assertTrue(any("Field 0201 length mismatch" in e for e in result.errors))

    def test_validate_sentence_missing_mandatory(self):
        parser = Parser()
        # Mock 'con0' missing 9103 (mandatory)
        tokens = [
             Token("8000", "con0", 1),
             # Missing 9103
             Token("9132", "Datenpaket1", 3)
        ]
        satz = Satz("con0", tokens)
        
        result = parser.validate_sentence(satz)
        self.assertFalse(result.valid)
        self.assertIn("Missing mandatory field 9103", result.errors)

    def test_validate_sentence_excess(self):
         parser = Parser()
         # Mock 'con9' which only allows 8000
         tokens = [
             Token("8000", "con9", 1),
             Token("9999", "Excess", 2)
         ]
         satz = Satz("con9", tokens)
         
         result = parser.validate_sentence(satz)
         self.assertFalse(result.valid)
         self.assertTrue(any("Excess tokens" in e for e in result.errors))

    def test_unknown_sentence_type(self):
        parser = Parser()
        satz = Satz("UNKNOWN_TYPE", [Token("8000", "UNKNOWN_TYPE", 1)])
        result = parser.validate_sentence(satz)
        self.assertFalse(result.valid)
        self.assertIn("Unknown sentence type: UNKNOWN_TYPE", result.errors)

if __name__ == '__main__':
    unittest.main()
