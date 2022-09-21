from dressings_manager_service.dressing.domain.dressing import Dressing
from dressings_manager_service.entrypoint.items.dressing_item import DressingItem


def get_dressing():
    id_ = "5"
    name = "5name"
    type_ = "5type_"
    tissue_treating = "5tissue_treating"
    exudate_compatibility = "5exudate_compatibility"
    treated_location = "5treated_location"
    fight_tunneling= "5fight_tunneling"
    fight_bad_olor = "5fight_bad_olor"
    adhesive = "5adhesive"
    hemostatic = "5hemostatic"
    instructions_to_use_es = "5instructions_to_use_es"
    instructions_to_use_gal = "5instructions_to_use_gal"
    instructions_to_use_eng = "5instructions_to_use_eng"
    dressing = Dressing(id_, name, type_, tissue_treating, exudate_compatibility, treated_location, fight_tunneling, fight_bad_olor, adhesive, hemostatic, instructions_to_use_es, instructions_to_use_gal, instructions_to_use_eng)
    return dressing


def get_dressing_item():
    id_ = "id_"
    name = "name"
    type_ = "type_"
    tissue_treating = "tissue_treating"
    exudate_compatibility = "exudate_compatibility"
    treated_location = "treated_location"
    fight_tunneling= "fight_tunneling"
    fight_bad_olor = "fight_bad_olor"
    adhesive = "adhesive"
    hemostatic = "hemostatic"
    instructions_to_use_es = "instructions_to_use_es"
    instructions_to_use_gal = "instructions_to_use_gal"
    instructions_to_use_eng = "instructions_to_use_eng"
    dressing_item = DressingItem(id_=id_, name=name, type_=type_, tissue_treating=tissue_treating, exudate_compatibility=exudate_compatibility, treated_location=treated_location, fight_tunneling=fight_tunneling, fight_bad_olor=fight_bad_olor, adhesive=adhesive, hemostatic=hemostatic, instructions_to_use_es=instructions_to_use_es, instructions_to_use_gal=instructions_to_use_gal, instructions_to_use_eng=instructions_to_use_eng)
    return dressing_item

def get_dressing_to_update():
    id_ = "73"
    name = "73name"
    type_ = "73type_"
    tissue_treating = "73tissue_treating"
    exudate_compatibility = "73exudate_compatibility"
    treated_location = "73treated_location"
    fight_tunneling= "73fight_tunneling"
    fight_bad_olor = "73fight_bad_olor"
    adhesive = "73adhesive"
    hemostatic = "73hemostatic"
    instructions_to_use_es = "73instructions_to_use_es"
    instructions_to_use_gal = "73instructions_to_use_gal"
    instructions_to_use_eng = "73instructions_to_use_eng"
    dressing = Dressing(id_, name, type_, tissue_treating, exudate_compatibility, treated_location, fight_tunneling, fight_bad_olor, adhesive, hemostatic, instructions_to_use_es, instructions_to_use_gal, instructions_to_use_eng)
    return dressing

    