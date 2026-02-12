import sys
import os
import argparse
from .reader import Reader
from .parser import Parser

def main():
    parser = argparse.ArgumentParser(description="Parse and validate KVDT files.")
    parser.add_argument("filename", help="Path to the KVDT file.")
    parser.add_argument("--storage", choices=["mongo", "json"], help="Optional storage sink.")
    parser.add_argument("--outdir", default=".", help="Output directory for JSON storage.")
    parser.add_argument("--uri", default="mongodb://localhost:27017/", help="MongoDB URI.")
    args = parser.parse_args()

    print(f"Reading file: {args.filename}")
    
    reader = Reader(args.filename)
    parser_obj = Parser()
    
    sentences = []
    errors = 0
    
    for satz in reader:
        sentences.append(satz)
        res = parser_obj.validate_sentence(satz)
        if not res.valid:
            errors += 1
            print(f"Error in sentence {len(sentences)} ({satz.type}):")
            for err in res.errors:
                print(f"  - {err}")
    
    print(f"\nProcessed {len(sentences)} sentences.")
    
    if args.storage:
        from .storage import MongoSink, JsonSink
        sink = None
        if args.storage == "mongo":
            sink = MongoSink(uri=args.uri)
        elif args.storage == "json":
            sink = JsonSink(output_dir=args.outdir)
        
        if sink:
            package_name = os.path.basename(args.filename).replace(".con", "")
            sink.save(package_name, sentences)

    if errors == 0:
        print("File is valid.")
    else:
        print(f"Found errors in {errors} sentences.")
        sys.exit(1)

if __name__ == "__main__":
    main()
