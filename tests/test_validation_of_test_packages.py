import os
import unittest

from src.pykvdt.parser import Parser
from src.pykvdt.reader import Reader

class TestValidationOfTestPackages(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = "test_packages_realistic"
        self.parser = Parser()

    def test_all_packages(self):
        if not os.path.exists(self.test_data_dir):
            self.skipTest(f"Directory {self.test_data_dir} does not exist.")

        files = [f for f in os.listdir(self.test_data_dir) if f.endswith(".con")]
        if not files:
            self.skipTest(f"No .con files found in {self.test_data_dir}.")

        for filename in files:
            filepath = os.path.join(self.test_data_dir, filename)
            with self.subTest(filename=filename):
                reader = Reader(filepath)
                sentences = list(reader)

                self.assertGreater(len(sentences), 0, f"File {filename} is empty.")
                
                for i, satz in enumerate(sentences):
                    result = self.parser.validate_sentence(satz)
                    if not result.valid:
                        errors = "\n".join(str(e) for e in result.errors)
                        msg = (
                            f"Validation failed for {filename}, "
                            f"Satz {i} ({satz.type}):\n{errors}"
                        )
                        self.fail(msg)

if __name__ == "__main__":
    unittest.main()
