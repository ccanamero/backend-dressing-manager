from dressings_manager_service.collagenase.domain.collagenase import Collagenase
from dressings_manager_service.entrypoint.items.collagenase_item import CollagenaseItem


def get_collagenase():
    id_ = "16"
    name = "16Collagenase"
    collagenase = Collagenase(id_, name)
    return collagenase


def get_collagenase_item():
    id_ = "8"
    name = "8Collagenase"
    collagenase_item = CollagenaseItem(id_=id_, name=name)
    return collagenase_item
