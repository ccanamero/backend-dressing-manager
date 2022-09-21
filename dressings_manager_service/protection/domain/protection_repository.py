import abc

from dressings_manager_service.protection.domain.protection import Protection


class ProtectionRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, protection: Protection):
        pass

    def update(self, protection: Protection):
        #comming soon
        pass

    def remove(self, protection: Protection):
        #comming soon
        pass
    
    def read(self, protection: Protection):
        #comming soon
        pass
