from unittest.mock import Mock

from dressings_manager_service.dressing.application.dressing_remover import DressingRemover
from tests.dressings_manager_service.dressing.utils import dressing_mother

def test_calls_dressing_repository_to_remove():
    dressing_repository = Mock()
    dressing_repository.store = Mock()    # ??
    dressing_remover = DressingRemover(dressing_repository)
    dressing = dressing_mother.get_dressing()
    dressing_remover.invoke(dressing)
    dressing_repository.remove.assert_called_once_with(dressing)
