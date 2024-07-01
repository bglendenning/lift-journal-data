from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from lift_journal_data.db.manage import create_tables


class TestCaseDb(TestCase):
    def setUp(self):
        # Use in-memory SQLite database
        self.engine = create_engine("sqlite://")
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        create_tables(self.engine)

    def tearDown(self):
        # Delete in-memory SQLite database
        self.engine.dispose()
