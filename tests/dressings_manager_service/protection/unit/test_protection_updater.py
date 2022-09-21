from unittest.mock import Mock

from dressings_manager_service.protection.application.protection_creator import ProtectionCreator
from tests.dressings_manager_service.protection.utils import protection_mother

def test_calls_protection_repository_to_read():
    protection_repository = Mock()
    protection_repository.store = Mock()    # ??
    protection_creator = ProtectionCreator(protection_repository)
    protection = protection_mother.get_protection()
    protection_creator.invoke(protection)
    protection_repository.store.assert_called_once_with(protection)
