from unittest.mock import Mock

from dressings_manager_service.dressing.application.dressing_creator import DressingCreator
from tests.dressings_manager_service.dressing.utils import dressing_mother

def test_calls_dressing_repository_to_create():
    dressing_repository = Mock()
    dressing_repository.store = Mock()    # ??
    dressing_creator = DressingCreator(dressing_repository)
    dressing = dressing_mother.get_dressing()
    dressing_creator.invoke(dressing)
    dressing_repository.store.assert_called_once_with(dressing)
