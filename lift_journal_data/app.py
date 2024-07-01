import argparse

from lift_journal_data.db import engine, SessionLocal
from lift_journal_data.db.manage import create_tables, drop_tables, load_lifts
from lift_journal_data.db.models import Lift


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--create-tables",
        action=argparse.BooleanOptionalAction,
        help="Create tables in the database.",
    )
    parser.add_argument(
        "--drop-tables",
        action=argparse.BooleanOptionalAction,
        help="Drop all tables in the database.",
    )
    parser.add_argument(
        "--load-lifts",
        action=argparse.BooleanOptionalAction,
        help="Populate the lift table with various lifts",
    )
    args = parser.parse_args()

    if args.create_tables:
        create_tables(engine)

    if args.drop_tables:
        drop_tables(engine)

    if args.load_lifts:
        load_lifts(SessionLocal, Lift)
