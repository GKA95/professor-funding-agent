import os
from datetime import datetime
from zoneinfo import ZoneInfo

TARGET_HOUR = 9
TARGET_MINUTE = 0

def is_send_time(timezone_name: str) -> bool:
    if not timezone_name:
        return False
    try:
        now = datetime.now(ZoneInfo(timezone_name))
        return now.hour == TARGET_HOUR and now.minute == TARGET_MINUTE
    except Exception:
        return False

def send_email_stub(to, subject, body):
    # DRY RUN until Gmail OAuth/API is connected.
    print("=" * 60)
    print("DRY RUN - EMAIL NOT SENT")
    print("TO:", to)
    print("SUBJECT:", subject)
    print(body)
    print("=" * 60)

if __name__ == "__main__":
    print("Email sender is in safe DRY RUN mode.")
    print("Gmail authentication must be configured before real sending.")
