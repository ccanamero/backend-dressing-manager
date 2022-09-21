from pydantic import BaseModel


class CollectionItem(BaseModel):
    id_: str
    name: str
    hospital: str
