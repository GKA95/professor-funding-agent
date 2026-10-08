from datetime import datetime, timezone

def eligible_candidates(candidates, minimum_score=75, daily_limit=5, contacted=None):
    contacted = {x.lower().strip() for x in (contacted or set())}
    fresh = [
        p for p in candidates
        if p.score >= minimum_score
        and p.email
        and p.email.lower().strip() not in contacted
    ]
    fresh.sort(key=lambda p: p.score, reverse=True)
    return fresh[:daily_limit]

def queue_record(p):
    return {
        "professor": p.name,
        "university": p.university,
        "email": p.email,
        "score": p.score,
        "timezone": p.timezone,
        "target_local_time": "09:00",
        "status": "QUEUED",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
