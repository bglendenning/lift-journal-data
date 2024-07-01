from pydantic import BaseModel


class LiftSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True
