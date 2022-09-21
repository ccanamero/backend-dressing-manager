from unittest.mock import Mock

from dressings_manager_service.collagenase.application.collagenase_reader import CollagenaseReader
from tests.dressings_manager_service.collagenase.utils import collagenase_mother

def test_calls_collagenase_repository_to_read():
    collagenase_repository = Mock()
    collagenase_repository.store = Mock()   
    collagenase_reader = CollagenaseReader(collagenase_repository)
    collagenase = collagenase_mother.get_collagenase()
    collagenase_reader.invoke(collagenase)
    collagenase_repository.read.assert_called_once_with(collagenase)
