from unittest.mock import Mock

from dressings_manager_service.collagenase.application.collagenase_remover import CollagenaseRemover
from tests.dressings_manager_service.collagenase.utils import collagenase_mother

def test_calls_collagenase_repository_to_remove():
    collagenase_repository = Mock()
    collagenase_repository.store = Mock()   
    collagenase_remover = CollagenaseRemover(collagenase_repository)
    collagenase = collagenase_mother.get_collagenase()
    collagenase_remover.invoke(collagenase)
    collagenase_repository.remove.assert_called_once_with(collagenase)
