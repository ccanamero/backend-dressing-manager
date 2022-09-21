from unittest.mock import Mock

from dressings_manager_service.collagenase.application.collagenase_creator import CollagenaseCreator
from tests.dressings_manager_service.collagenase.utils import collagenase_mother

def test_calls_collagenase_repository_to_create():
    collagenase_repository = Mock()
    collagenase_repository.store = Mock()  
    collagenase_creator = CollagenaseCreator(collagenase_repository)
    collagenase = collagenase_mother.get_collagenase()
    collagenase_creator.invoke(collagenase)
    collagenase_repository.store.assert_called_once_with(collagenase)
