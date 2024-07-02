import unittest

from pydantic_core import ValidationError

from lift_journal_data.schemas.user import UserCreateSchema


class TestUserCreateSchema(unittest.TestCase):
    email = "email@domain.tld"

    def test_valid(self):
        user_register = UserCreateSchema(
            email=self.email,
            password="password",
        )
        self.assertEqual(user_register.email, self.email)
        self.assertEqual(user_register.password, "password")

    def test_email_invalid(self):
        with self.assertRaises(ValidationError) as context:
            UserCreateSchema(
                email="",
                password="password",
            )
        self.assertIn("email", str(context.exception))

    def test_password_invalid(self):
        with self.assertRaises(ValidationError) as context:
            UserCreateSchema(
                email=self.email,
                password="",
            )
        self.assertIn("password", str(context.exception))
