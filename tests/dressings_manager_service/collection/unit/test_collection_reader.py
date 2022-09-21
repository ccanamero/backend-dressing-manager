from unittest.mock import Mock

from dressings_manager_service.collection.application.collection_reader import CollectionReader
from tests.dressings_manager_service.collection.utils import collection_mother

def test_calls_collection_repository_to_read():
    collection_repository = Mock()
    collection_repository.store = Mock()   
    collection_reader = CollectionReader(collection_repository)
    collection = collection_mother.get_collection()
    collection_reader.invoke(collection)
    collection_repository.read.assert_called_once_with(collection)
