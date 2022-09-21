from tests.dressings_manager_service.protection.utils import protection_mother

def test_stores_one_protection(mysql_protection_repository_setup_and_teardown):
    mysql_protection_repository = mysql_protection_repository_setup_and_teardown
    protection = protection_mother.get_protection()
    mysql_protection_repository.store(protection)
    protections = mysql_protection_repository.retrieve(protection.id_)
    mysql_protection_repository._commit_and_close_connection() # commit changes and close database connection
    assert (protections.name == protection.name)


def test_updates_one_protection(mysql_protection_repository_setup_and_teardown):
    mysql_protection_repository = mysql_protection_repository_setup_and_teardown
    protection = protection_mother.get_protection_to_modify()
    protection.name = "updateName"
    protection.type_ = "updateType"
    mysql_protection_repository.update(protection)
    protections = mysql_protection_repository.retrieve(protection.id_)
    mysql_protection_repository._commit_and_close_connection() # commit changes and close database connection
    assert protections.name == protection.name


def test_removes_one_protection(mysql_protection_repository_setup_and_teardown):
    mysql_protection_repository = mysql_protection_repository_setup_and_teardown
    protection = protection_mother.get_protection()
    mysql_protection_repository.remove(protection.id_)
    protections = mysql_protection_repository.retrieve(protection.id_)
    mysql_protection_repository._commit_and_close_connection() # commit changes and close database connection
    assert (protections.name != protection.name)  