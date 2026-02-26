import argparse
from .storage import add_entry, list_entries, get_data_file_path
from .validators import validate_mood, validate_sleep, validate_drug, validate_date


def main():
    parser = argparse.ArgumentParser(description="Mood Journal CLI v0.1")
    subparsers = parser.add_subparsers(dest="command")

    # ADD
    add_parser = subparsers.add_parser("add", help="Add new entry")
    add_parser.add_argument("--mood", required=True)
    add_parser.add_argument("--sleep", required=True)
    add_parser.add_argument("--drug", required=True)
    add_parser.add_argument("--note", default="")
    add_parser.add_argument("--date", default=None)

    # LIST
    list_parser = subparsers.add_parser("list", help="List recent entries")
    list_parser.add_argument("--n", type=int, default=7)

    # WHERE
    subparsers.add_parser("where", help="Show data file location")

    args = parser.parse_args()

    if args.command == "add":
        mood = validate_mood(args.mood)
        sleep = validate_sleep(args.sleep)
        drug = validate_drug(args.drug)
        date = validate_date(args.date)

        entry = add_entry(mood, sleep, drug, args.note, date)
        print(
            f"Saved: {entry['date']} mood={entry['mood']} "
            f"sleep={entry['sleep_hours']} drug={entry['drug']}"
        )

    elif args.command == "list":
        entries = list_entries(args.n)
        print(f"{'DATE':<12}{'MOOD':<6}{'SLEEP':<8}{'DRUG':<6}NOTE")
        for e in entries:
            print(
                f"{e['date']:<12}{e['mood']:<6}"
                f"{e['sleep_hours']:<8}{e['drug']:<6}{e['note']}"
            )

    elif args.command == "where":
        print(f"Data file: {get_data_file_path()}")

    else:
        parser.print_help()