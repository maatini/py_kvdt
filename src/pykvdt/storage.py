import json
import os
from abc import ABC, abstractmethod
from typing import List
from .model import Satz

class DataSink(ABC):
    """Abstract base class for KVDT data storage sinks."""

    @abstractmethod
    def save(self, package_name: str, sentences: List[Satz]):
        """Saves a list of KVDT sentences to the sink."""
        pass

class JsonSink(DataSink):
    """Stores KVDT package data as a JSON file."""

    def __init__(self, output_dir: str = "."):
        self.output_dir = output_dir

    def save(self, package_name: str, sentences: List[Satz]):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        filename = f"{package_name}.json"
        filepath = os.path.join(self.output_dir, filename)
        
        data = [s.to_dict() for s in sentences]
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Saved package to {filepath}")

class MongoSink(DataSink):
    """Stores KVDT package data in a MongoDB collection."""

    def __init__(self, uri: str = "mongodb://localhost:27017/", database: str = "pykvdt", collection: str = "packages"):
        try:
            from pymongo import MongoClient
            self.client = MongoClient(uri)
            self.db = self.client[database]
            self.collection = self.db[collection]
        except ImportError:
            raise ImportError("pymongo is required for MongoSink. Install it with 'pip install pymongo'.")

    def save(self, package_name: str, sentences: List[Satz]):
        document = {
            "package_name": package_name,
            "sentences": [s.to_dict() for s in sentences]
        }
        
        # Use upsert or unique identifier if needed, for now just insert
        result = self.collection.insert_one(document)
        print(f"Stored package '{package_name}' in MongoDB (ID: {result.inserted_id})")
