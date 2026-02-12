import unittest
from src.pykvdt.generator import Generator
from src.pykvdt.parser import Parser
from src.pykvdt.model import Satz

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.parser = Parser()

    def test_generate_simple_sentence_con9(self):
        """Test generating a simple sentence type 'con9' (only 8000 field)."""
        satz = self.generator.generate_sentence("con9")
        self.assertIsInstance(satz, Satz)
        self.assertEqual(satz.type, "con9")
        self.assertTrue(len(satz.tokens) > 0)
        self.assertEqual(satz.tokens[0].type, "8000")
        
        # Verify validity
        result = self.parser.validate_sentence(satz)
        self.assertTrue(result.valid, f"Generated con9 sentence is invalid: {result.errors}")

    def test_generate_complex_sentence_0101(self):
        """Test generating a complex sentence type '0101' with groups."""
        satz = self.generator.generate_sentence("0101")
        self.assertIsInstance(satz, Satz)
        self.assertEqual(satz.type, "0101")
        
        # Verify validity
        result = self.parser.validate_sentence(satz)
        self.assertTrue(result.valid, f"Generated 0101 sentence is invalid: {result.errors}")

    def test_generate_all_types(self):
        """Smoke test to generate all defined sentence types."""
        from src.pykvdt.structures import SENTENCE_TYPES
        for satz_type in SENTENCE_TYPES:
            with self.subTest(satz_type=satz_type):
                satz = self.generator.generate_sentence(satz_type)
                result = self.parser.validate_sentence(satz)
                self.assertTrue(result.valid, f"Generated {satz_type} sentence is invalid: {result.errors}")

    def test_generate_full_file(self):
        """Test generating a full KVDT file structure."""
        sentences = self.generator.generate_kvdt_file()
        self.assertTrue(len(sentences) >= 6) # con0, besa, adt0, at least 1 case, adt9, con9
        
        # Verify structure order (basic check)
        self.assertEqual(sentences[0].type, "con0")
        self.assertEqual(sentences[1].type, "besa")
        self.assertEqual(sentences[2].type, "adt0")
        self.assertEqual(sentences[-2].type, "adt9")
        self.assertEqual(sentences[-1].type, "con9")
        
        # Verify consistency of BSNR (Field 0201/0217/0218)
        # 1. Identify BSNR from besa (tokens are 0201 usually)
        besa_bsnr = None
        for t in sentences[1].tokens:
            if t.type == "0201":
                besa_bsnr = t.attr
                break
        
        self.assertIsNotNone(besa_bsnr, "BESA record should have BSNR (0201)")
        
        # 2. Check if other records use the same BSNR where applicable
        for i, s in enumerate(sentences):
            for t in s.tokens:
                if t.type in ["0201", "0217", "0218"]:
                    # Note: besa has multiple 0201 if multiple NBSNRs exist, 
                    # but our generator currently uses one context.bsnr.
                    # So they should all match the context.
                    self.assertEqual(t.attr, self.generator.context.bsnr, f"BSNR mismatch in sentence {i} ({s.type}) field {t.type}")

        # Verify LANR consistency
        # LANRs used in 0212, 4241, 4242, 5099 must be in context.lanrs
        for i, s in enumerate(sentences):
            for t in s.tokens:
                if t.type in ["0212", "4241", "4242", "5099"]:
                    self.assertIn(t.attr, self.generator.context.lanrs, f"LANR {t.attr} in sentence {i} ({s.type}) field {t.type} not in generated context")

if __name__ == '__main__':
    unittest.main()
