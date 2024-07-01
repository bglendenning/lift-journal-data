from sqlalchemy import inspect

from lift_journal_data.db.manage import create_tables, drop_tables, load_lifts
from lift_journal_data.db.models import Lift
from tests.db import TestCaseDb


class TestModels(TestCaseDb):
    tables = ["user", "lift"]

    def test_create_tables(self):
        with self.SessionLocal() as session:
            create_tables(self.engine)
            inspector = inspect(session.get_bind())

            for table in self.tables:
                self.assertTrue(inspector.has_table(table))

    def test_drop_tables(self):
        with self.SessionLocal() as session:
            create_tables(self.engine)
            drop_tables(self.engine)
            inspector = inspect(session.get_bind())

            for table in self.tables:
                self.assertFalse(inspector.has_table(table))

    def test_load_lifts(self):
        with self.SessionLocal() as session:
            load_lifts(session, Lift)
            lifts = session.query(Lift).all()
            self.assertEqual(len(lifts), 12)
