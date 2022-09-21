from pydantic import BaseModel


class CollagenaseItem(BaseModel):
    id_: str
    name: str
