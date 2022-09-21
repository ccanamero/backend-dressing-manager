from unittest.mock import Mock

from dressings_manager_service.dressing.application.dressing_reader import DressingReader
from tests.dressings_manager_service.dressing.utils import dressing_mother

def test_calls_dressing_repository_to_read():
    dressing_repository = Mock()
    dressing_repository.store = Mock()    # ??
    dressing_reader = DressingReader(dressing_repository)
    dressing = dressing_mother.get_dressing()
    dressing_reader.invoke(dressing)
    dressing_repository.read.assert_called_once_with(dressing)
