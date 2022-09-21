from dressings_manager_service.collection.domain.collection import Collection
from dressings_manager_service.entrypoint.items.collection_item import CollectionItem


def get_collection():
    id_ = "6"
    name = "6name"
    hospital = "6hospital"
    collection = Collection(id_, name, hospital)
    return collection


def get_collection_item():
    id_ = "6"
    name = "6name"
    hospital = "6hospital"
    collection_item = CollectionItem(id_=id_, name=name, hospital=hospital)
    return collection_item

def get_collection_to_modify():
    id_ = "73"
    name = "73name"
    hospital = "73hospital"
    collection = Collection(id_, name, hospital)
    return collection
