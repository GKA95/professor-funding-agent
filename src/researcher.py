from .models import Professor

def discover_candidates():
    """Starter discovery interface.

    The first version deliberately returns an empty list. This keeps the
    repository safe until a permitted search/data source is connected.
    Later this function will connect to the selected research source(s).
    """
    return []

def normalize_candidate(raw):
    return Professor(
        name=raw.get("name", "").strip(),
        university=raw.get("university", "").strip(),
        department=raw.get("department", "").strip(),
        country=raw.get("country", "").strip(),
        state=raw.get("state", "").strip(),
        email=raw.get("email", "").strip(),
        research_area=raw.get("research_area", "").strip(),
        research_url=raw.get("research_url", "").strip(),
        funding_evidence=raw.get("funding_evidence", "").strip(),
        latest_publication=raw.get("latest_publication", "").strip(),
        timezone=raw.get("timezone", "").strip(),
    )
