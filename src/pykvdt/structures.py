from typing import List, Union
from .model import SentenceDefinition, FieldReference, GroupReference, FieldDefinition
# Note: In a full implementation, I would import all definitions or use string references.

# Helper to make definitions less verbose
def F(id: str, mandatory: bool = True, count: int = 1, rules: List[str] = None) -> FieldReference:
    return FieldReference(field_id=id, mandatory=mandatory, count=count, rules=rules or [])

def G(items: List[Union[FieldReference, GroupReference]], mandatory: bool = True, count: int = 1, rules: List[str] = None) -> GroupReference:
    return GroupReference(items=items, mandatory=mandatory, count=count, rules=rules or [])

# Structures
CON0 = SentenceDefinition(
    id="con0",
    name="Container Start",
    structure=[
        F("8000"),
        F("9103"),
        G([
            F("9132", count=-1)
        ], rules=[])
    ]
)

CON9 = SentenceDefinition(
    id="con9",
    name="Container End",
    structure=[F("8000")]
)

BESA = SentenceDefinition(
    id="besa",
    name="Bestandsdaten",
    structure=[
        F("8000"),
        F("0201", count=-1),
        F("0203"),
        G([
            F("0219", mandatory=False),
            F("0220", mandatory=False),
            F("0221", mandatory=False),
            F("0211", rules=["R719"]),
            F("0222", mandatory=False)
        ], count=-1),
        F("0205"),
        F("0215"),
        F("0216"),
        F("0208"),
        F("0209", mandatory=False),
        F("0218", mandatory=False)
    ]
)

# ... (Adding more structures as needed)

SENTENCES = {
    "con0": CON0,
    "con9": CON9,
    "besa": BESA,
}

