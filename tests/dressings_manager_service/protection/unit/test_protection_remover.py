from unittest.mock import Mock

from dressings_manager_service.protection.application.protection_remover import ProtectionRemover
from tests.dressings_manager_service.protection.utils import protection_mother

def test_calls_protection_repository_to_read():
    protection_repository = Mock()
    protection_repository.store = Mock()    # ??
    protection_remover = ProtectionRemover(protection_repository)
    protection = protection_mother.get_protection()
    protection_remover.invoke(protection)
    protection_repository.remove.assert_called_once_with(protection)
