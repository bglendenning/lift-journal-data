from pydantic import BaseModel


class LiftSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
