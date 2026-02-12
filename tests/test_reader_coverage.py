import unittest
import os
import tempfile
from src.pykvdt.reader import Reader
from src.pykvdt.model import Token
from src.pykvdt.exceptions import KVDTReaderError

class TestReaderCoverage(unittest.TestCase):
    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            reader = Reader(tmp_path)
            sentences = list(reader)
            self.assertEqual(len(sentences), 0)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_malformed_lines_raise_error(self):
        # Lines shorter than 7 chars should raise KVDTReaderError
        content = b"123\n0048000Test\n12\n"
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        
        try:
            reader = Reader(tmp_path)
            with self.assertRaises(KVDTReaderError) as cm:
                list(reader)
            self.assertIn("Line too short", str(cm.exception))
            self.assertEqual(cm.exception.line_nbr, 1)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_encoding_latin1(self):
        # Test reading file with latin1 chars
        content = "0108000Muller\n0109999Österreich\n".encode('iso-8859-15')
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
            
        try:
            reader = Reader(tmp_path, encoding='iso-8859-15')
            sentences = list(reader)
            # Output: 1 sentence (starts with 8000), 2 tokens
            self.assertEqual(len(sentences), 1)
            self.assertEqual(len(sentences[0].tokens), 2)
            self.assertEqual(sentences[0].tokens[1].attr, "Österreich")
        finally:
             if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_mixed_line_endings_stripping(self):
        # Verify rstrip logic: 
        # Line 1: Unix LF
        # Line 2: Windows CRLF
        # Line 3: Whitespace content (should be preserved)
        content = b"0068000LF\n0089999CRLF\r\n0121234  SPACE \n"
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
            
        try:
            reader = Reader(tmp_path)
            sentences = list(reader)
            self.assertEqual(len(sentences), 1)
            tokens = sentences[0].tokens
            self.assertEqual(len(tokens), 3)
            self.assertEqual(tokens[0].attr, "LF")
            self.assertEqual(tokens[1].attr, "CRLF")
            self.assertEqual(tokens[2].attr, "  SPACE ") # Should prefer internal/trailing space
        finally:
             if os.path.exists(tmp_path):
                os.remove(tmp_path)

if __name__ == '__main__':
    unittest.main()
