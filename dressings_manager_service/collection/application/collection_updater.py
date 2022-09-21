from dressings_manager_service.collection.domain.collection import Collection
from dressings_manager_service.collection.domain.collection_repository import CollectionRepository


class CollectionUpdater:
    def __init__(self, collection_repository: CollectionRepository):
        self.collection_repository = collection_repository

    def invoke(self, collection: Collection):
        self.collection_repository.update(collection)
