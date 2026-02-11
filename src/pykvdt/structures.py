from typing import List, Union
from .model import SentenceDefinition, FieldReference, GroupReference

def F(id: str, mandatory: bool = True, count: int = 1, rules: List[str] = None) -> FieldReference:
    return FieldReference(field_id=id, mandatory=mandatory, count=count, rules=rules or [])

def G(items: List[Union[FieldReference, GroupReference]], mandatory: bool = True, count: int = 1, rules: List[str] = None) -> GroupReference:
    return GroupReference(items=items, mandatory=mandatory, count=count, rules=rules or [])

Leistungen = [
    F("5001"),
    F("5002", mandatory=False),
    F("5005", mandatory=False),
    F("5006", mandatory=False),
    F("5008", mandatory=False),
    F("5009", mandatory=False, count=-1),
    G([
        F("5011", count=-1),
    ], mandatory=False, count=-1, rules=[]),
    F("5013", mandatory=False),
    F("5015", mandatory=False, count=-1),
    F("5016", mandatory=False, count=-1),
    F("5017", mandatory=False, rules=['(lambda kontext: (kontext["Satzart"] in ["0101", "0102", "0104"]))']),
    F("5018", mandatory=False),
    F("5019", mandatory=False),
    G([
        F("5021", mandatory=False),
    ], mandatory=False, count=1, rules=[]),
    F("5023", mandatory=False),
    F("5024", mandatory=False),
    F("5025", mandatory=False),
    F("5026", mandatory=False),
    F("5034", mandatory=False),
    G([
        F("5041", mandatory=False),
    ], mandatory=False, count=-1, rules=[]),
    F("5036", mandatory=False, count=-1),
    F("5037", rules=['Simultaneingriff']),
    F("5038", mandatory=False, count=-1),
    F("5040", mandatory=False),
    G([
        F("5043"),
    ], mandatory=False, count=1, rules=[]),
    F("5044", mandatory=False, rules=['(lambda kontext: (kontext["Satzart"] in ["0102"]))']),
    F("5070", rules=['R770']),
    G([
        F("5072", count=-1, rules=['R772']),
        F("5073", count=-1, rules=['R773']),
    ], mandatory=True, count=1, rules=['R770']),
    F("5098"),
    F("5099"),
]

ICD_Codes = [
    G([
        F("6003", rules=['R484']),
        F("6004", mandatory=False),
        F("6006", mandatory=False, count=-1),
        F("6008", count=-1, rules=['R491']),
    ], mandatory=True, count=-1, rules=['R486', 'R488', 'R489', 'R761', 'R490', 'R491', 'R492', 'R728', 'R729']),
]

Dauerdiagnosen = [
    G([
        F("3674"),
        F("3675", mandatory=False),
        F("3676", mandatory=False, count=-1),
        F("3677", count=-1, rules=['R491']),
    ], mandatory=True, count=-1, rules=['R486', 'R488', 'R489', 'R761', 'R490', 'R491', 'R492', 'R728', 'R729']),
]

con0 = SentenceDefinition(
    id="con0",
    name="con0",
    structure=[
        F("8000"),
        F("9103"),
        G([
            F("9132", count=-1),
        ], mandatory=True, count=1, rules=[]),
    ]
)

con9 = SentenceDefinition(
    id="con9",
    name="con9",
    structure=[
        F("8000"),
    ]
)

besa = SentenceDefinition(
    id="besa",
    name="besa",
    structure=[
        F("8000"),
        F("0201", count=-1),
        F("0203"),
        G([
            F("0219", mandatory=False),
            F("0220", mandatory=False),
            F("0221", mandatory=False),
            F("0211", rules=['R719']),
            F("0222", mandatory=False),
        ], mandatory=True, count=-1, rules=[]),
        F("0205"),
        F("0215"),
        F("0216"),
        F("0208"),
        F("0209", mandatory=False),
        F("0218", mandatory=False),
    ]
)

rvsa = SentenceDefinition(
    id="rvsa",
    name="rvsa",
    structure=[
        F("8000", rules=['R743']),
        G([
            G([
                G([
                    G([
                        F("0303"),
                    ], mandatory=True, count=-1, rules=['R741']),
                ], mandatory=True, count=1, rules=['R740']),
                G([
                    F("0305"),
                ], mandatory=True, count=-1, rules=['R740']),
            ], mandatory=True, count=1, rules=[]),
        ], mandatory=True, count=-1, rules=[]),
    ]
)

adt0 = SentenceDefinition(
    id="Satzart",
    name="adt0",
    structure=[
        F("8000"),
        F("0105"),
        F("9102"),
        F("9212"),
        F("0102"),
        F("0121"),
        F("0122"),
        F("0123"),
        F("0124"),
        F("0125", mandatory=False),
        F("0111", mandatory=False),
        F("0126"),
        F("0127"),
        F("0128"),
        F("0129"),
        F("0130"),
        F("0131", mandatory=False),
        F("0103"),
        F("0132", mandatory=False),
        F("9115", mandatory=False),
        G([
            F("9261"),
        ], mandatory=False, count=1, rules=[]),
        F("9204"),
        F("9250", mandatory=False, count=-1),
    ]
)

adt9 = SentenceDefinition(
    id="adt9",
    name="adt9",
    structure=[
        F("8000"),
    ]
)

s0101 = SentenceDefinition(
    id="0101",
    name="s0101",
    structure=[
        F("8000"),
        F("3000", mandatory=False),
        F("3003", mandatory=False),
        F("3004", rules=['R306']),
        F("3006", rules=['R397']),
        F("3100", mandatory=False),
        F("3101"),
        F("3102"),
        F("3103"),
        F("3104", mandatory=False),
        F("3105", rules=['R752']),
        F("3119", rules=['R752']),
        F("3107", mandatory=False),
        F("3112", rules=['R479']),
        F("3114", mandatory=False),
        F("3113", mandatory=False),
        F("3116", mandatory=False),
        F("3108"),
        F("3110"),
        F("4101"),
        F("4102", mandatory=False),
        F("4104"),
        F("4106"),
        F("4108", mandatory=False),
        F("4109", rules=['VERSICHERTENKARTE']),
        F("4110", rules=['R752']),
        F("4111"),
        F("4112", rules=['R752']),
        F("4113", rules=['R752']),
        F("4121"),
        F("4122"),
        F("4123", mandatory=False),
        F("4124", mandatory=False),
        F("4125", mandatory=False),
        F("4126", mandatory=False, count=-1),
        F("4202", mandatory=False),
        F("4204", mandatory=False),
        F("4206", mandatory=False),
        G([
            G([
                F("4247", mandatory=False),
                G([
                    F("4245"),
                    F("4246"),
                ], mandatory=False, count=-1, rules=[]),
            ], mandatory=True, count=-1, rules=[]),
        ], mandatory=False, count=1, rules=[]),
        F("4236", mandatory=False),
        F("4239"),
        G([
            *Leistungen, 
        ], mandatory=True, count=-1, rules=[]),
        *ICD_Codes,
        *Dauerdiagnosen,
    ]
)

s0102 = SentenceDefinition(
    id="0102",
    name="s0102",
    structure=[
        F("8000"),
        F("3000", mandatory=False),
        F("3003", mandatory=False),
        F("3004", rules=['R306']),
        F("3006", rules=['R397']),
        F("3100", mandatory=False),
        F("3101"),
        F("3102"),
        F("3103"),
        F("3104", mandatory=False),
        F("3105", rules=['R752']),
        F("3119", rules=['R752']),
        F("3107", mandatory=False),
        F("3112", rules=['R479']),
        F("3114", mandatory=False),
        F("3113", mandatory=False),
        F("3116", mandatory=False),
        F("3108"),
        F("3110"),
        F("4101"),
        F("4102", mandatory=False),
        F("4104"),
        F("4106"),
        F("4108", mandatory=False),
        F("4109", rules=['VERSICHERTENKARTE']),
        F("4110", rules=['R752']),
        F("4111"),
        F("4112", rules=['R752']),
        F("4113", rules=['R752']),
        F("4121"),
        F("4122"),
        F("4123", mandatory=False),
        F("4124", mandatory=False),
        F("4125", mandatory=False),
        F("4126", mandatory=False, count=-1),
        F("4202", mandatory=False),
        F("4204", mandatory=False),
        F("4205", count=-1, rules=['R744', 'R755']),
        F("4206", mandatory=False),
        F("4207", mandatory=False, count=-1),
        F("4208", mandatory=False, count=-1),
        G([
            F("4241"),
        ], mandatory=False, count=1, rules=['R431']),
        G([
            F("4242"),
        ], mandatory=True, count=1, rules=['R328']),
        F("4219", rules=['R328']),
        F("4220", rules=['R320']),
        F("4221", rules=['R404']),
        F("4229", mandatory=False, rules=['R432']),
        G([
            G([
                F("4247", mandatory=False),
                G([
                    F("4245"),
                    F("4246"),
                ], mandatory=False, count=-1, rules=[]),
            ], mandatory=True, count=-1, rules=[]),
        ], mandatory=False, count=1, rules=[]),
        F("4239"),
        G([
            *Leistungen,
        ], mandatory=True, count=-1, rules=[]),
        *ICD_Codes,
        *Dauerdiagnosen,
    ]
)

s0103 = SentenceDefinition(
    id="0103",
    name="s0103",
    structure=[
        F("8000"),
        F("3000", mandatory=False),
        F("3003", mandatory=False),
        F("3004", rules=['R306']),
        F("3006", rules=['R397']),
        F("3100", mandatory=False),
        F("3101"),
        F("3102"),
        F("3103"),
        F("3104", mandatory=False),
        F("3105", rules=['R752']),
        F("3119", rules=['R752']),
        F("3107", mandatory=False),
        F("3112", rules=['R479']),
        F("3114", mandatory=False),
        F("3113", mandatory=False),
        F("3116", mandatory=False),
        F("3108"),
        F("3110"),
        F("4101"),
        F("4102", mandatory=False),
        F("4104"),
        F("4106"),
        F("4108", mandatory=False),
        F("4109", rules=['VERSICHERTENKARTE']),
        F("4110", rules=['R752']),
        F("4111"),
        F("4112", rules=['R752']),
        F("4113", rules=['R752']),
        F("4121"),
        F("4122"),
        F("4123", mandatory=False),
        F("4124", mandatory=False),
        F("4126", mandatory=False, count=-1),
        F("4202", mandatory=False),
        F("4204", mandatory=False),
        F("4205", count=-1, rules=['R746']),
        F("4206", mandatory=False),
        F("4207", count=-1, rules=['R746']),
        F("4208", count=-1, rules=['R746']),
        G([
            F("4242"),
        ], mandatory=True, count=1, rules=['R746']),
        F("4233", count=-1, rules=['R354']),
        F("4239"),
        G([
            *Leistungen, 
        ], mandatory=True, count=-1, rules=[]),
        *ICD_Codes,
        *Dauerdiagnosen,
    ]
)

s0104 = SentenceDefinition(
    id="0104",
    name="s0104",
    structure=[
        F("8000"),
        F("3000", mandatory=False),
        F("3003", mandatory=False),
        F("3004", rules=['R306']),
        F("3006", rules=['R397']),
        F("3100", mandatory=False),
        F("3101"),
        F("3102"),
        F("3103"),
        F("3104", mandatory=False),
        F("3105", rules=['R752']),
        F("3119", rules=['R752']),
        F("3107", mandatory=False),
        F("3112", rules=['R479']),
        F("3114", mandatory=False),
        F("3113", mandatory=False),
        F("3116", mandatory=False),
        F("3108"),
        F("3110"),
        F("4101"),
        F("4104"),
        F("4106"),
        F("4108", mandatory=False),
        F("4109", rules=['VERSICHERTENKARTE']),
        F("4133", rules=['R775']),
        F("4110", rules=['R752']),
        F("4111"),
        F("4112", rules=['R752']),
        F("4113", rules=['R752']),
        F("4121"),
        F("4122"),
        F("4123", mandatory=False),
        F("4124", mandatory=False),
        F("4125", mandatory=False),
        F("4126", mandatory=False, count=-1),
        F("4202", mandatory=False),
        F("4239"),
        F("4243"),
        G([
            *Leistungen,
        ], mandatory=True, count=-1, rules=[]),
        *ICD_Codes,
        *Dauerdiagnosen,
    ]
)

SENTENCE_TYPES = {
    "con0": con0,
    "con9": con9,
    "besa": besa,
    "rvsa": rvsa,
    "adt0": adt0,
    "adt9": adt9,
    "0101": s0101,
    "0102": s0102,
    "0103": s0103,
    "0104": s0104,
}
