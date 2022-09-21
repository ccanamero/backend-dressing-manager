
from tests.dressings_manager_service.collection.utils import collection_mother

def test_stores_one_collection(mysql_collection_repository_setup_and_teardown):
    mysql_collection_repository = mysql_collection_repository_setup_and_teardown
    collection = collection_mother.get_collection()
    mysql_collection_repository.store(collection)
    collections = mysql_collection_repository.retrieve(collection.id_)
    mysql_collection_repository._commit_and_close_connection() # commit changes and close database connection
    assert (collections.name == collection.name)


def test_updates_one_collection(mysql_collection_repository_setup_and_teardown):
    mysql_collection_repository = mysql_collection_repository_setup_and_teardown
    collection = collection_mother.get_collection_to_modify()
    collection.name = "updateName"
    collection.hospital = "updateHospital"
    mysql_collection_repository.update(collection)
    collections = mysql_collection_repository.retrieve(collection.id_)
    mysql_collection_repository._commit_and_close_connection() # commit changes and close database connection
    assert collections.name == collection.name


def test_removes_one_collection(mysql_collection_repository_setup_and_teardown):
    mysql_collection_repository = mysql_collection_repository_setup_and_teardown
    collection = collection_mother.get_collection()
    mysql_collection_repository.remove(collection.id_)
    collections = mysql_collection_repository.retrieve(collection.id_)
    mysql_collection_repository._commit_and_close_connection() # commit changes and close database connection
    assert (collections.name != collection.name)


""" def test_read_all_collections(mysql_collection_repository_setup_and_teardown):
    mysql_collection_repository = mysql_collection_repository_setup_and_teardown
    collections = mysql_collection_repository.retrieveAll()
    mysql_collection_repository._commit_and_close_connection() # commit changes and close database connection
    assert bool(collections) """
