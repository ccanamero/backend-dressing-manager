from pydantic import BaseModel


class DressingItem(BaseModel):
    id_: str
    name: str
    type_: str
    tissue_treating: str
    exudate_compatibility: str #bool
    treated_location: str 
    fight_tunneling: str #bool
    fight_bad_olor: str #bool
    adhesive: str #bool
    hemostatic: str #bool
    instructions_to_use_es: str
    instructions_to_use_gal: str
    instructions_to_use_eng: str
