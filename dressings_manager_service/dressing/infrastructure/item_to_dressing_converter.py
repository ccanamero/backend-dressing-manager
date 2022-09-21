from dressings_manager_service.dressing.domain.dressing import Dressing
from dressings_manager_service.entrypoint.items.dressing_item import DressingItem


def invoke(dressing_item: DressingItem) -> Dressing:
    return Dressing(
        dressing_item.id_,
        dressing_item.name,
        dressing_item.type_,
        dressing_item.tissue_treating,
        dressing_item.exudate_compatibility,
        dressing_item.treated_location,
        dressing_item.fight_tunneling,
        dressing_item.fight_bad_olor,
        dressing_item.adhesive,
        dressing_item.hemostatic,
        dressing_item.instructions_to_use_es,
        dressing_item.instructions_to_use_gal,
        dressing_item.instructions_to_use_eng,
    )