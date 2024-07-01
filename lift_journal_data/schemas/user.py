from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo


class UserSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

    @field_validator("password")
    @classmethod
    def check_empty(cls, value: str, info: ValidationInfo) -> str:
        if not value:
            raise ValueError(f"{info.field_name} cannot be empty")

        return value
