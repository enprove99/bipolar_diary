from datetime import datetime
import sys


def validate_mood(value):
    try:
        mood = int(value)
        if 1 <= mood <= 5:
            return mood
    except ValueError:
        pass
    sys.exit("Error: mood must be integer between 1-5.")


def validate_sleep(value):
    try:
        sleep = float(value)
        if 0 <= sleep <= 24:
            return sleep
    except ValueError:
        pass
    sys.exit("Error: sleep must be number between 0-24.")


def validate_drug(value):
    value = value.lower()
    if value in ("yes", "no"):
        return value
    sys.exit("Error: drug must be 'yes' or 'no'.")


def validate_date(value):
    if value is None:
        return datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value
    except ValueError:
        sys.exit("Error: date must be YYYY-MM-DD.")