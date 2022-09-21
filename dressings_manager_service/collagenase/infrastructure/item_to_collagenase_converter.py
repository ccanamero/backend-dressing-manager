from dressings_manager_service.collagenase.domain.collagenase import Collagenase
from dressings_manager_service.entrypoint.items.collagenase_item import CollagenaseItem


def invoke(collagenase_item: CollagenaseItem) -> Collagenase:
    return Collagenase(
        collagenase_item.id_,
        collagenase_item.name,
    )