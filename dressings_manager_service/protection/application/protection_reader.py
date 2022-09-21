from dressings_manager_service.protection.domain.protection import Protection
from dressings_manager_service.protection.domain.protection_repository import ProtectionRepository


class ProtectionReader:
    def __init__(self, protection_repository: ProtectionRepository):
        self.protection_repository = protection_repository

    def invoke(self, protection: Protection):
        self.protection_repository.read(protection)
