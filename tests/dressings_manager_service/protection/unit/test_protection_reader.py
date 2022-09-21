from unittest.mock import Mock

from dressings_manager_service.protection.application.protection_reader import ProtectionReader
from tests.dressings_manager_service.protection.utils import protection_mother

def test_calls_protection_repository_to_read():
    protection_repository = Mock()
    protection_repository.store = Mock()    # ??
    protection_reader = ProtectionReader(protection_repository)
    protection = protection_mother.get_protection()
    protection_reader.invoke(protection)
    protection_repository.read.assert_called_once_with(protection)
