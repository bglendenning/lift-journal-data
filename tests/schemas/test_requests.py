import unittest

from pydantic_core import ValidationError

from lift_journal_data.schemas.user import UserCreate


class TestUserCreate(unittest.TestCase):
    email = "email@domain.tld"

    def test_valid(self):
        """UserCreate is valid."""

        user_register = UserCreate(
            email=self.email,
            password1="password",
            password2="password",
        )
        self.assertEqual(user_register.email, self.email)
        self.assertEqual(user_register.password1, "password")
        self.assertEqual(user_register.password2, "password")

    def test_email_invalid(self):
        """UserCreate.email is invalid."""

        with self.assertRaises(ValidationError) as context:
            user_register = UserCreate(
                email="email",
                password1="password",
                password2="password",
            )
        self.assertIn("email", str(context.exception))

    def test_password_invalid(self):
        """UserCreate.password1 or password2 are invalid."""

        with self.assertRaises(ValidationError) as context:
            user_register = UserCreate(
                email=self.email,
                password1="",
                password2="password",
            )
        self.assertIn("password1", str(context.exception))

    def test_passwords_do_not_match(self):
        """UserCreate.password1 and password2 do not match."""

        with self.assertRaises(ValidationError) as context:
            user_register = UserCreate(
                email=self.email,
                password1="password1",
                password2="password2",
            )
        self.assertIn("Passwords do not match", str(context.exception))
