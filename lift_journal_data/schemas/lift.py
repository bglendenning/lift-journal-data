from pydantic import BaseModel


class LiftCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
