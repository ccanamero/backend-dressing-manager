from unittest.mock import Mock

from dressings_manager_service.collection.application.collection_creator import CollectionCreator
from tests.dressings_manager_service.collection.utils import collection_mother

def test_calls_collection_repository_to_create():
    collection_repository = Mock()
    collection_repository.store = Mock()    # ??
    collection_creator = CollectionCreator(collection_repository)
    collection = collection_mother.get_collection()
    collection_creator.invoke(collection)
    collection_repository.store.assert_called_once_with(collection)
