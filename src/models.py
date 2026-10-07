from dataclasses import dataclass
from typing import Optional

@dataclass
class Professor:
    name: str
    university: str
    department: str = ""
    country: str = ""
    state: str = ""
    email: str = ""
    research_area: str = ""
    research_url: str = ""
    funding_evidence: str = ""
    latest_publication: str = ""
    timezone: str = ""
    score: int = 0
    status: str = "NEW"
