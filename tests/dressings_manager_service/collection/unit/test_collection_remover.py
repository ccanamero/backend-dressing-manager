from unittest.mock import Mock

from dressings_manager_service.collection.application.collection_remover import CollectionRemover
from tests.dressings_manager_service.collection.utils import collection_mother

def test_calls_collection_repository_to_remover():
    collection_repository = Mock()
    collection_repository.store = Mock()   
    collection_remover = CollectionRemover(collection_repository)
    collection = collection_mother.get_collection()
    collection_remover.invoke(collection)
    collection_repository.remove.assert_called_once_with(collection)
