from dressings_manager_service.collection.domain.collection import Collection
from dressings_manager_service.entrypoint.items.collection_item import CollectionItem


def invoke(collection_item: CollectionItem) -> Collection:
    return Collection(
        collection_item.id_,
        collection_item.name,
        collection_item.hospital,
    )