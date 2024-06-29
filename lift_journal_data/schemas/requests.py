from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo


class UserRegister(BaseModel):
    email: EmailStr
    password1: str
    password2: str

    @field_validator("*")
    @classmethod
    def check_empty(cls, value: str, info: ValidationInfo) -> str:
        if not value:
            raise ValueError(f"{info.field_name} cannot be empty")

        return value
