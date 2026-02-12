from dataclasses import dataclass
from typing import Optional, List, Union

@dataclass
class Token:
    """Represents a single KVDT token (field)."""
    type: str  # The 4-digit field identifier (e.g., '8000', '0201')
    attr: str  # The value of the field
    line_nbr: int

    def to_bytes(self) -> bytes:
        """Converts the token to bytes representation (Length + Type + Content + CR + LF)."""
        content = self.attr.encode('iso-8859-1')
        type_bytes = self.type.encode('iso-8859-1')
        length = len(content) + len(type_bytes) + 3 + 2 # +3 for length field itself (3 digits), +2 for CRLF
        return f"{length:03d}".encode('iso-8859-1') + type_bytes + content + b'\r\n'

@dataclass
class Satz:
    """Represents a KVDT sentence (a collection of tokens starting with 8000)."""
    type: str
    tokens: List[Token]
    
    @property
    def Satzart(self) -> str:
        return self.type

    def to_bytes(self) -> bytes:
        """Converts the sentence to bytes."""
        return b''.join(t.to_bytes() for t in self.tokens)

@dataclass
class ValidationErrorObject:
    """Detailed information about a validation error."""
    message: str
    field_id: Optional[str] = None
    line_nbr: Optional[int] = None
    satz_type: Optional[str] = None

    def __str__(self) -> str:
        context = []
        if self.satz_type: context.append(f"Satz {self.satz_type}")
        if self.line_nbr: context.append(f"Line {self.line_nbr}")
        if self.field_id: context.append(f"Field {self.field_id}")
        
        ctx_str = f"[{', '.join(context)}] " if context else ""
        return f"{ctx_str}{self.message}"

@dataclass
class ValidationResult:
    """Result of a validation operation."""
    valid: bool
    errors: List[ValidationErrorObject]

@dataclass
class FieldDefinition:
    """Definition of a KVDT field."""
    id: str
    description: str
    min_len: int
    max_len: int
    type: str # 'a', 'n', 'd', 'g', 'z'
    
@dataclass
class SentenceDefinition:
    """Definition of a KVDT sentence structure."""
    id: str
    name: str
    structure: List[Union['FieldReference', 'GroupReference']]

@dataclass
class FieldReference:
    """Reference to a field within a sentence structure."""
    field_id: str
    mandatory: bool # True = 'm', False = 'k'
    count: int # -1 for unlimited
    rules: List[str]

@dataclass
class GroupReference:
    """Reference to a group of fields within a sentence structure."""
    items: List[Union['FieldReference', 'GroupReference']]
    mandatory: bool
    count: int
    rules: List[str]
