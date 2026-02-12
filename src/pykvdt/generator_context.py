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
    
    def __post_init__(self):
        # Generate at least one doctor if none provided
        if not self.lanrs:
            self.lanrs.append("999999900") # Default fallback
            # Add some random ones
            for _ in range(random.randint(1, 3)):
                self.lanrs.append("".join(random.choices(string.digits, k=9)))

    def get_random_lanr(self) -> str:
        return random.choice(self.lanrs)
