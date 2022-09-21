from tests.dressings_manager_service.collagenase.utils import collagenase_mother

def test_stores_one_collagenase(mysql_collagenase_repository_setup_and_teardown):
    mysql_collagenase_repository = mysql_collagenase_repository_setup_and_teardown
    collagenase = collagenase_mother.get_collagenase()
    mysql_collagenase_repository.store(collagenase)
    collagenases = mysql_collagenase_repository.retrieve(collagenase.id_)
    mysql_collagenase_repository._commit_and_close_connection() # commit changes and close database connection
    assert (collagenases.name == collagenase.name)


def test_updates_one_collagenase(mysql_collagenase_repository_setup_and_teardown):
    mysql_collagenase_repository = mysql_collagenase_repository_setup_and_teardown
    collagenase = collagenase_mother.get_collagenase()
    collagenase.name = "updateName"
    mysql_collagenase_repository.update(collagenase)
    collagenases = mysql_collagenase_repository.retrieve(collagenase.id_)
    mysql_collagenase_repository._commit_and_close_connection() # commit changes and close database connection
    assert collagenases.name == collagenase.name


def test_removes_one_collagenase(mysql_collagenase_repository_setup_and_teardown):
    mysql_collagenase_repository = mysql_collagenase_repository_setup_and_teardown
    collagenase = collagenase_mother.get_collagenase()
    mysql_collagenase_repository.remove(collagenase.id_)
    collagenases = mysql_collagenase_repository.retrieve(collagenase.id_)
    mysql_collagenase_repository._commit_and_close_connection() # commit changes and close database connection
    assert (collagenases.name != collagenase.name)
