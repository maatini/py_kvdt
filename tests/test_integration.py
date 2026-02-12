import unittest
import os
import tempfile
from src.pykvdt.generator import Generator
from src.pykvdt.reader import Reader
from src.pykvdt.parser import Parser

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.parser = Parser()

    def test_e2e_pipeline(self):
        """
        End-to-End Test:
        1. Generate a KVDT file structure in memory
        2. Write it to a temporary file
        3. Read it back using Reader
        4. Validate it using Parser
        """
        # 1. Generate
        sentences = self.generator.generate_kvdt_file()
        
        # 2. Write
        with tempfile.NamedTemporaryFile(suffix=".con", delete=False) as tmp:
            tmp_path = tmp.name
            for satz in sentences:
                tmp.write(satz.to_bytes())
        
        try:
            # 3. Read
            reader = Reader(tmp_path)
            read_sentences = list(reader)
            
            self.assertEqual(len(read_sentences), len(sentences), "Read different number of sentences than generated")
            
            # 4. Validate
            for i, satz in enumerate(read_sentences):
                result = self.parser.validate_sentence(satz)
                self.assertTrue(result.valid, f"Validation failed for sentence {i} ({satz.type}): {result.errors}")
                
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == '__main__':
    unittest.main()
