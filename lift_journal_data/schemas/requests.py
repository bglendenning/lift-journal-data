from typing_extensions import Self

from pydantic import BaseModel, EmailStr, field_validator, model_validator, ValidationInfo


class UserCreate(BaseModel):
    email: EmailStr
    password1: str
    password2: str

    class Config:
        from_attributes = True

    @field_validator("password1", "password2")
    @classmethod
    def check_empty(cls, value: str, info: ValidationInfo) -> str:
        if not value:
            raise ValueError(f"{info.field_name} cannot be empty")

        return value

    @model_validator(mode="after")
    def passwords_match(self) -> Self:
        password1 = self.password1
        password2 = self.password2

        if password1 != password2:
            raise ValueError("Passwords do not match")

        return self
