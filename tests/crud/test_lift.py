from lift_journal_data.crud.lift import LiftDAO
from lift_journal_data.db.manage import load_lifts
from tests.db import TestCaseDb


class TestUserDAO(TestCaseDb):
    def test_get_all(self):
        db_lifts = LiftDAO(self.SessionLocal()).get_all()
        self.assertFalse(db_lifts)

        load_lifts(self.SessionLocal())
        db_lifts = LiftDAO(self.SessionLocal()).get_all()
        self.assertTrue(db_lifts)
