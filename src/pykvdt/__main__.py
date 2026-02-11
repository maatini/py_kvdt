import sys
import argparse
from .reader import Reader
from .parser import Parser

def main():
    parser = argparse.ArgumentParser(description="Parse and validate KVDT files.")
    parser.add_argument("filename", help="Path to the KVDT file.")
    args = parser.parse_args()

    print(f"Reading file: {args.filename}")
    
    reader = Reader(args.filename)
    parser_obj = Parser()
    
    count = 0
    errors = 0
    
    for satz in reader:
        count += 1
        res = parser_obj.validate_sentence(satz)
        if not res.valid:
            errors += 1
            print(f"Error in sentence {count} ({satz.type}):")
            for err in res.errors:
                print(f"  - {err}")
    
    print(f"\nProcessed {count} sentences.")
    if errors == 0:
        print("File is valid.")
    else:
        print(f"Found errors in {errors} sentences.")
        sys.exit(1)

if __name__ == "__main__":
    main()
