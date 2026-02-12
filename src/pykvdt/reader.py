import typing
from .model import Token, Satz
from .exceptions import KVDTReaderError

class Reader:
    """
    Reads a KVDT file and yields parsed sentences as `Satz` objects.
    
    The reader handles the binary-to-text conversion (ISO-8859-15) and 
    splits the field stream into logical sentences based on the '8000' field.
    """

    def __init__(self, filename: str, encoding: str = "ISO-8859-15"):
        """
        Initializes the Reader.
        
        Args:
            filename: Path to the KVDT (.con) file.
            encoding: Text encoding (default: ISO-8859-15).
        """
        self.filename = filename
        self.encoding = encoding

    def __iter__(self) -> typing.Iterator[Satz]:
        """
        Iterates over the file and yields `Satz` objects.
        
        Yields:
            Satz: A parsed KVDT sentence containing tokens.
            
        Raises:
            KVDTReaderError: If a line is malformed or too short.
        """
        with open(self.filename, 'r', encoding=self.encoding) as f:
            current_tokens: typing.List[Token] = []
            
            for line_nbr, line in enumerate(f, start=1):
                # Only strip newline characters, preserve internal/trailing whitespace
                line = line.rstrip('\n').rstrip('\r')
                if not line.strip():
                    continue
                
                # Basic parsing based on fixed width: LLL KKKK Content
                # LLL = length (3 bytes), KKKK = type (4 bytes)
                # We assume the file is line-delimited for now as per legacy reader.
                if len(line) < 7:
                    raise KVDTReaderError("Line too short (min 7 bytes for LLLKKKK)", line_nbr=line_nbr)

                try:
                    # length_str = line[0:3]
                    field_type = line[3:7]
                    field_value = line[7:]
                except Exception as e:
                    raise KVDTReaderError(f"Failed to parse line: {e}", line_nbr=line_nbr)

                token = Token(type=field_type, attr=field_value, line_nbr=line_nbr)
                # print(f"DEBUG: '{line}' -> Type: '{field_type}', Attr: '{field_value}'")

                if token.type == "8000":
                    if current_tokens:
                        yield self._create_satz(current_tokens)
                    current_tokens = [token]
                else:
                    current_tokens.append(token)
            
            if current_tokens:
                yield self._create_satz(current_tokens)

    def _create_satz(self, tokens: typing.List[Token]) -> Satz:
        # The first token should be 8000, which defines the sentence type
        sentence_type = tokens[0].attr if tokens and tokens[0].type == '8000' else "UNKNOWN"
        return Satz(type=sentence_type, tokens=tokens)
