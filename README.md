py_kvdt
=======

Python library for parsing and validating KVDT files (KBV Datentransfer).

## Features

- **Modern structure**: Clean package layout with type hints and dataclasses.
- **Validation**: Checks field lengths, types, and sentence structures.
- **No dependencies**: Uses standard library only.

## Installation

1. Clone the repository: `git clone https://github.com/maatini/py_kvdt.git`
2. Navigate to the directory: `cd py_kvdt`
3. Install (editable mode): `pip install -e .`

## Usage

### CLI
Run the parser on a KVDT file:

```bash
python3 -m src.pykvdt <path_to_file>
```

### Library
```python
from src.pykvdt.reader import Reader
from src.pykvdt.parser import Parser

reader = Reader("path/to/file.con")
parser = Parser()

for satz in reader:
    result = parser.validate_sentence(satz)
    if not result.valid:
        print(result.errors)
```

## Legacy Code
The original 2014 implementation is available in the `legacy/` directory.

## License
GPL v3. See LICENCE file.





