import json
from pathlib import Path
from .models import Professor

def load_profile():
    return json.loads(Path("config/profile.json").read_text(encoding="utf-8"))

def score_professor(p: Professor, profile=None):
    profile = profile or load_profile()
    text = " ".join([
        p.research_area, p.funding_evidence, p.latest_publication
    ]).lower()

    primary = [x.lower() for x in profile["primary_fields"]]
    secondary = [x.lower() for x in profile["secondary_fields"]]

    primary_hits = sum(1 for x in primary if x in text)
    secondary_hits = sum(1 for x in secondary if x in text)

    # Starter scoring model. We will replace this with AI-assisted scoring later.
    research = min(30, primary_hits * 6 + secondary_hits * 2)
    funding = 20 if p.funding_evidence.strip() else 0
    publication = 10 if p.latest_publication.strip() else 0
    email = 10 if p.email.strip() else 0
    university = 10 if p.university.strip() else 0
    research_url = 5 if p.research_url.strip() else 0
    field_match = min(15, primary_hits * 3)

    p.score = min(100, research + funding + publication + email +
                   university + research_url + field_match)
    return p

if __name__ == "__main__":
    demo = Professor(
        name="Demo Professor",
        university="Example University",
        email="professor@example.edu",
        research_area="Microgrids, renewable energy, battery energy storage and machine learning",
        funding_evidence="Research project funding mentioned on university page",
        latest_publication="Recent paper on energy forecasting",
        research_url="https://example.edu"
    )
    print(score_professor(demo))
