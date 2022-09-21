from dressings_manager_service.protection.domain.protection import Protection
from dressings_manager_service.entrypoint.items.protection_item import ProtectionItem


def get_protection():
    id_ = "5"
    name = "5name"
    type_ = "5type_"
    protection = Protection(id_, name, type_)
    return protection


def get_protection_item():
    id_ = "5"
    name = "5name"
    type_ = "5type_"
    protection_item = ProtectionItem(id_=id_, name=name, type_=type_)
    return protection_item

def get_protection_to_modify():
    id_ = "73"
    name = "updatedName"
    type_ = "upadtedType"
    protection = Protection(id_, name, type_)
    return protection
