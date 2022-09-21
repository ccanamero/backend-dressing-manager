from unittest.mock import Mock

from dressings_manager_service.collagenase.application.collagenase_updater import CollagenaseUpdater
from tests.dressings_manager_service.collagenase.utils import collagenase_mother

def test_calls_collagenase_repository_to_update():
    collagenase_repository = Mock()
    collagenase_repository.store = Mock()   
    collagenase_updater = CollagenaseUpdater(collagenase_repository)
    collagenase = collagenase_mother.get_collagenase()
    collagenase_updater.invoke(collagenase)
    collagenase_repository.update.assert_called_once_with(collagenase)
