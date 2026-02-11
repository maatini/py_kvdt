from dataclasses import dataclass
from typing import Optional, List, Union

@dataclass
class Token:
    """Represents a single KVDT token (field)."""
    type: str  # The 4-digit field identifier (e.g., '8000', '0201')
    attr: str  # The value of the field
    line_nbr: int

@dataclass
class Satz:
    """Represents a KVDT sentence (a collection of tokens starting with 8000)."""
    type: str
    tokens: List[Token]
    
    @property
    def Satzart(self) -> str:
        return self.type

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
