import unittest
import os
import json
import shutil
from src.pykvdt.model import Satz, Token
from src.pykvdt.storage import JsonSink, MongoSink

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_output"
        self.sentences = [
            Satz(type="con0", tokens=[Token(type="8000", attr="con0", line_nbr=1)]),
            Satz(type="adt0", tokens=[Token(type="8000", attr="adt0", line_nbr=2)])
        ]

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_json_sink_save(self):
        sink = JsonSink(output_dir=self.test_dir)
        package_name = "test_package"
        sink.save(package_name, self.sentences)
        
        filepath = os.path.join(self.test_dir, f"{package_name}.json")
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["type"], "con0")
        self.assertEqual(data[0]["tokens"][0]["attr"], "con0")

    @unittest.skip("Requires a running MongoDB instance")
    def test_mongo_sink_save(self):
        # This test is skipped by default as it requires infra
        sink = MongoSink(database="pykvdt_test")
        sink.save("test_package", self.sentences)
        # In a real test we would verify the record in DB
        # self.assertEqual(sink.collection.count_documents({"package_name": "test_package"}), 1)

if __name__ == "__main__":
    unittest.main()
