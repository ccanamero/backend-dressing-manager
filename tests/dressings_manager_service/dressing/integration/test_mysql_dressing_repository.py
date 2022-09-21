
from tests.dressings_manager_service.dressing.utils import dressing_mother

def test_stores_one_dressing(mysql_dressing_repository_setup_and_teardown):
    mysql_dressing_repository = mysql_dressing_repository_setup_and_teardown
    dressing = dressing_mother.get_dressing()
    mysql_dressing_repository.store(dressing)
    dressings = mysql_dressing_repository.retrieve(dressing.id_)
    mysql_dressing_repository._commit_and_close_connection() # commit changes and close database connection
    assert (dressings.name == dressing.name)


def test_updates_one_dressing(mysql_dressing_repository_setup_and_teardown):
    mysql_dressing_repository = mysql_dressing_repository_setup_and_teardown
    dressing = dressing_mother.get_dressing_to_update()
    dressing.name = "updateName"
    dressing.type_ = "updateType_"
    dressing.tissue_treating = "updateTissue_treating"
    dressing.exudate_compatibility = "updateExudate_compatibility"
    dressing.treated_location = "updateTreated_location"
    dressing.fight_tunneling= "updateFight_tunneling"
    dressing.fight_bad_olor = "updateFight_bad_olor"
    dressing.adhesive = "updateAdhesive"
    dressing.hemostatic = "updateHemostatic"
    dressing.instructions_to_use_es = "updateInstructions_to_use_es"
    dressing.instructions_to_use_gal = "updateInstructions_to_use_gal"
    dressing.instructions_to_use_eng = "updateInstructions_to_use_eng"
    mysql_dressing_repository.update(dressing)
    dressings = mysql_dressing_repository.retrieve(dressing.id_)
    mysql_dressing_repository._commit_and_close_connection() # commit changes and close database connection
    assert dressings.name == dressing.name
    assert dressings.type_ == dressing.type_
    assert dressings.tissue_treating == dressing.tissue_treating
    assert dressings.exudate_compatibility == dressing.exudate_compatibility
    assert dressings.fight_tunneling == dressing.fight_tunneling
    assert dressings.fight_bad_olor == dressing.fight_bad_olor
    assert dressings.adhesive == dressing.adhesive
    assert dressings.hemostatic == dressing.hemostatic
    assert dressings.instructions_to_use_es == dressing.instructions_to_use_es
    assert dressings.instructions_to_use_gal == dressing.instructions_to_use_gal
    assert dressings.instructions_to_use_eng == dressing.instructions_to_use_eng



def test_removes_one_dressing(mysql_dressing_repository_setup_and_teardown):
    mysql_dressing_repository = mysql_dressing_repository_setup_and_teardown
    dressing = dressing_mother.get_dressing()
    mysql_dressing_repository.remove(dressing.id_)
    dressings = mysql_dressing_repository.retrieve(dressing.id_)
    mysql_dressing_repository._commit_and_close_connection() # commit changes and close database connection
    assert (dressings.name != dressing.name) 
