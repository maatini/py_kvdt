import random
import string
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class GeneratorContext:
    """
    Holds the state for a KVDT file generation process to ensure consistency.
    """
    bsnr: str = field(default_factory=lambda: "".join(random.choices(string.digits, k=9)))
    # List of LANRs available in this facility
    lanrs: List[str] = field(default_factory=list)
    
    # Realistic data pools
    _first_names: List[str] = field(default_factory=lambda: [
        "Thomas", "Michael", "Andreas", "Stefan", "Christian", "Petra", "Sabine", "Monika", "Susanne", "Claudia",
        "Julia", "Daniel", "Alexander", "Tobias", "Sarah", "Anna", "Laura", "Jan", "Lukas", "Leon"
    ])
    _last_names: List[str] = field(default_factory=lambda: [
        "Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann",
        "Bauer", "Richter", "Wolf", "Schröder", "Neumann", "Schwarz", "Zimmermann", "Braun", "Krüger", "Hofmann"
    ])
    _streets: List[str] = field(default_factory=lambda: [
        "Hauptstraße", "Bahnhofstraße", "Dorfstraße", "Schulstraße", "Gartenstraße", "Bergstraße", "Birkenweg", 
        "Lindenstraße", "Kirchstraße", "Eichenweg", "Ahornweg", "Waldstraße", "Feldstraße", "Ringstraße"
    ])
    _cities: List[tuple] = field(default_factory=lambda: [
        ("10115", "Berlin"), ("20095", "Hamburg"), ("80331", "München"), ("50667", "Köln"), ("60311", "Frankfurt am Main"),
        ("70173", "Stuttgart"), ("40213", "Düsseldorf"), ("04109", "Leipzig"), ("44137", "Dortmund"), ("45127", "Essen"),
        ("28195", "Bremen"), ("01067", "Dresden"), ("30159", "Hannover"), ("90403", "Nürnberg"), ("47051", "Duisburg")
    ])
    
    # EBM 2025 GOPs (Common codes)
    _gops: List[str] = field(default_factory=lambda: [
        "03000", "03001", "03002", "03003", "03004", "03005", # GP Basics
        "01430", "01435", # Communication
        "32001", # Urine test
        "01700", "01701", "01732", # Prevention / Checkup
        "01645", "04538", "13678", "40128", "03220", "03221" # Specific 2025 updates/common
    ])
    
    # ICD-10 Codes (Common diagnoses)
    _icds: List[str] = field(default_factory=lambda: [
        "J06.9", "I10", "E11.9", "M54.5", "J20.9", "F32.9", "K29.7", "R51", "Z01.7",
        "J00", "J01.9", "I11.9", "E11.90", "M54.4", "F41.1", "K21.9", "R10.4"
    ])
    
    # Diagnosis Certainty
    _diagnose_certainty: List[str] = field(default_factory=lambda: ["G", "V", "A", "Z"])
    
    # Insurance ID (eGK Versichertennummer)
    _egk_numbers: List[str] = field(default_factory=lambda: [
        "A123456789", "B987654321", "C555444333", "D111222333", "E000000000",
        "F123123123", "G456456456", "H789789789", "I098098098", "J135246357"
    ])
    
    # Insurance Status (Versichertenstatus, field 4112)
    _insurance_status: List[str] = field(default_factory=lambda: ["1000", "3000", "5000", "1001", "3001", "5001"])
    
    # KTAB (Kostenträgerabrechnungsbereich, field 4106)
    _ktab: List[str] = field(default_factory=lambda: ["00", "01", "02", "03", "04"])
    
    # Quartal (field 4101)
    _quarters: List[str] = field(default_factory=lambda: ["12025", "22025", "32025", "42025"])

    def __post_init__(self):
        # Generate at least one doctor if none provided
        if not self.lanrs:
            self.lanrs.append("999999900") # Default fallback
            # Add some random ones
            for _ in range(random.randint(1, 3)):
                self.lanrs.append("".join(random.choices(string.digits, k=9)))

    def get_random_lanr(self) -> str:
        return random.choice(self.lanrs)

    def get_first_name(self) -> str:
        return random.choice(self._first_names)
    
    def get_last_name(self) -> str:
        return random.choice(self._last_names)
        
    def get_street(self) -> str:
        return f"{random.choice(self._streets)} {random.randint(1, 150)}"
        
    def get_city_data(self) -> tuple:
        return random.choice(self._cities)
        
    def get_gop(self) -> str:
        return random.choice(self._gops)
        
    def get_icd(self) -> str:
        return random.choice(self._icds)
        
    def get_icd_3(self) -> str:
        # Return only the first 3 chars (e.g. J06) for restricted fields
        return random.choice(self._icds)[:3].replace(".", "")

    def get_diagnose_certainty(self) -> str:
        return random.choice(self._diagnose_certainty)

    def get_insurance_id(self) -> str:
        return random.choice(self._egk_numbers)

    def get_insurance_status(self) -> str:
        return random.choice(self._insurance_status)

    def get_ktab(self) -> str:
        return random.choice(self._ktab)

    def get_quarter(self) -> str:
        return random.choice(self._quarters)

