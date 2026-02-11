import unittest
import os
import tempfile
from src.pykvdt.reader import Reader
from src.pykvdt.model import Token, Satz

class TestReader(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='ISO-8859-15')
        # Standard valid content
        self.test_file.write("0158000con0\n")
        self.test_file.write("012910327012024\n")
        # Empty lines (should be ignored)
        self.test_file.write("\n")
        self.test_file.write("   \n")
        # Malformed lines (too short, should be ignored)
        self.test_file.write("123\n") 
        self.test_file.write("004123\n") # Length but no content? Actually Reader logic: len(line) < 7 check
        # Content with special chars (ISO-8859-15)
        self.test_file.write("0158000besa\n")
        # "Müller" in ISO-8859-15 is M\xfcller
        self.test_file.write(f"0150201M\xfcller\n") 

        self.test_file.close()

    def tearDown(self):
        os.unlink(self.test_file.name)

    def test_reader_parsing(self):
        reader = Reader(self.test_file.name)
        satze = list(reader)
        
        self.assertEqual(len(satze), 2)
        
        # Check first sentence (con0)
        s1 = satze[0]
        self.assertEqual(s1.type, "con0")
        self.assertEqual(len(s1.tokens), 2)
        self.assertEqual(s1.tokens[1].attr, "27012024")

        # Check second sentence (besa)
        s2 = satze[1]
        self.assertEqual(s2.type, "besa")
        self.assertEqual(len(s2.tokens), 2)
        # Check special char handling
        self.assertEqual(s2.tokens[1].attr, "Müller")

if __name__ == '__main__':
    unittest.main()
