import unittest

from lift_journal_data import crud, models
from lift_journal_data.schemas import requests


class TestUserCrud(unittest.TestCase):
    email = "email@domain.tld"

    def setUp(self):
        models.create_tables()

    def test_create_user(self):
        user = requests.UserCreate(
            email=self.email,
            password1="password",
            password2="password",
        )
        db_user = crud.create_user(user)
        self.assertEqual(db_user.email, self.email)

        # User exists for provided email
        db_user = crud.create_user(user)
        self.assertIs(db_user, None)
