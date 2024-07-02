from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo


def check_empty(value: str):
    if value:
        return True

    return False


class UserBaseSchema(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def check_email_empty(cls, value: str, info: ValidationInfo) -> str:
        if not check_empty(value):
            raise ValueError(f"{info.field_name} cannot be empty")

        return value


class UserCreateSchema(UserBaseSchema):
    password: str

    class Config:
        from_attributes = True

    @field_validator("password")
    @classmethod
    def check_password_empty(cls, value: str, info: ValidationInfo) -> str:
        if not check_empty(value):
            raise ValueError(f"{info.field_name} cannot be empty")

        return value


class UserReadSchema(UserBaseSchema):
    id: int
