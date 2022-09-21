from pydantic import BaseModel


class ProtectionItem(BaseModel):
    id_: str
    name: str
    type_: str
