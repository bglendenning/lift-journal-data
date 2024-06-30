import unittest

from lift_journal_data import models


class TestModels(unittest.TestCase):
    def setUp(self):
        models.create_tables()

    def tearDown(self):
        # Delete in-memory SQLite database
        models.engine.dispose()

    def test_load_lifts(self):
        with models.SessionLocal() as self.session:
            models.load_lifts()
            lifts = self.session.query(models.Lift).all()
            self.assertEqual(len(lifts), 12)
