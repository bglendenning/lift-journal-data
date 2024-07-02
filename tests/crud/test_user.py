from lift_journal_data.crud.user import UserDAO
from lift_journal_data.schemas.user import UserCreateSchema
from tests.db import TestCaseDb


class TestUserDAO(TestCaseDb):
    user = UserCreateSchema(
        email="email@domain.tld",
        password="password",
    )

    def test_create(self):
        db_user = UserDAO(self.SessionLocal()).create(self.user)
        self.assertEqual(db_user.email, self.user.email)

    def test_create_with_existing_email(self):
        UserDAO(self.SessionLocal()).create(self.user)
        db_user = UserDAO(self.SessionLocal()).create(self.user)
        self.assertIs(db_user, None)

    def test_get_for_email(self):
        UserDAO(self.SessionLocal()).create(self.user)
        db_user = UserDAO(self.SessionLocal()).get_for_email(self.user.email)
        self.assertEqual(db_user.email, self.user.email)

        db_user = UserDAO(self.SessionLocal()).get_for_email(f"1{self.user.email}")
        self.assertEqual(db_user, None)
