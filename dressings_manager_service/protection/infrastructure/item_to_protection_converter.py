from dressings_manager_service.protection.domain.protection import Protection
from dressings_manager_service.entrypoint.items.protection_item import ProtectionItem


def invoke(protection_item: ProtectionItem) -> Protection:
    return Protection(
        protection_item.id_,
        protection_item.name,
        protection_item.type_,
    )