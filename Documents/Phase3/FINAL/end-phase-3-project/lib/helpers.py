from datetime import datetime

def to_iso_format(dt):
    return dt.isoformat()

def from_iso_format(date_str):
    return datetime.fromisoformat(date_str)
