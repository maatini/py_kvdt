import os
import argparse
from src.pykvdt.generator import Generator

def main():
    parser = argparse.ArgumentParser(description="Generate KVDT test data files.")
    parser.add_argument("--count", type=int, default=1, help="Number of files to generate")
    parser.add_argument("--outdir", type=str, default="./test_data", help="Output directory")
    parser.add_argument("--min-cases", type=int, default=5, help="Minimum number of cases per file")
    parser.add_argument("--max-cases", type=int, default=10, help="Maximum number of cases per file")
    args = parser.parse_args()

    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)

    print(f"Generating {args.count} files in {args.outdir} with {args.min_cases}-{args.max_cases} cases per file...")

    for i in range(args.count):
        generator = Generator()
        sentences = generator.generate_kvdt_file(min_cases=args.min_cases, max_cases=args.max_cases)
        
        filename = f"testfile_{i:03d}.con"
        filepath = os.path.join(args.outdir, filename)
        
        with open(filepath, "wb") as f:
            for satz in sentences:
                f.write(satz.to_bytes())
        
        print(f"  Created {filename} ({len(sentences)} sentences)")

    print("Done.")

if __name__ == "__main__":
    main()
