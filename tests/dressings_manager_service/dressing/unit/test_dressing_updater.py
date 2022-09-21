from unittest.mock import Mock

from dressings_manager_service.dressing.application.dressing_updater import DressingUpdater
from tests.dressings_manager_service.dressing.utils import dressing_mother

def test_calls_dressing_repository_to_update():
    dressing_repository = Mock()
    dressing_repository.store = Mock()    # ??
    dressing_updater = DressingUpdater(dressing_repository)
    dressing = dressing_mother.get_dressing()
    dressing_updater.invoke(dressing)
    dressing_repository.update.assert_called_once_with(dressing)
