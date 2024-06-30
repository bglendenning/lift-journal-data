import unittest

from lift_journal_data import models
from sqlalchemy import inspect


class TestModels(unittest.TestCase):
    tables = ["user", "lift"]

    def setUp(self):
        models.create_tables()

    def tearDown(self):
        # Delete in-memory SQLite database
        models.engine.dispose()

    def test_create_tables(self):
        with models.SessionLocal() as self.session:
            models.create_tables()
            inspector = inspect(self.session.get_bind())

            for table in self.tables:
                self.assertTrue(inspector.has_table(table))

    def test_drop_tables(self):
        with models.SessionLocal() as self.session:
            models.create_tables()
            models.drop_tables()
            inspector = inspect(self.session.get_bind())

            for table in self.tables:
                self.assertFalse(inspector.has_table(table))

    def test_load_lifts(self):
        with models.SessionLocal() as self.session:
            models.load_lifts()
            lifts = self.session.query(models.Lift).all()
            self.assertEqual(len(lifts), 12)
