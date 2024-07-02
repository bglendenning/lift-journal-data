import json
import os
from pathlib import Path

from lift_journal_data.db import Base


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
