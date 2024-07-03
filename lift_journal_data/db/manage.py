import argparse
import json
import os
from pathlib import Path

from lift_journal_data.db import Base, LiftJournalData
from lift_journal_data.db.models import Lift


def create_tables(engine):
    Base.metadata.create_all(engine)


def drop_tables(engine):
    Base.metadata.drop_all(engine)


def load_lifts(session, lift_orm):
    with session:
        with open(Path(os.path.dirname(__file__)) / "../fixtures/lifts.json") as lifts_json:
            lifts = [lift_orm(name=lift["name"]) for lift in json.load(lifts_json)]

        session.add_all(lifts)
        session.commit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--create-tables",
        action=argparse.BooleanOptionalAction,
        help="Create all tables in the database if they do not exist",
    )
    parser.add_argument(
        "--drop-tables",
        action=argparse.BooleanOptionalAction,
        help="Drop all tables in the database if they exist",
    )
    parser.add_argument(
        "--load-lifts",
        action=argparse.BooleanOptionalAction,
        help="Populate the lift table with fixture data",
    )
    args = parser.parse_args()

    if args.drop_tables:
        drop_tables(LiftJournalData().engine)
        print("Dropped tables.")

    if args.create_tables:
        create_tables(LiftJournalData().engine)
        print("Created tables.")

    if args.load_lifts:
        load_lifts(LiftJournalData().SessionLocal(), Lift)
        print("Loaded lifts.")


if __name__ == "__main__":
    main()
