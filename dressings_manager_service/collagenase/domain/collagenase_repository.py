import abc

from dressings_manager_service.collagenase.domain.collagenase import Collagenase


class CollagenaseRepository(abc.ABC):

    @abc.abstractmethod
    def store(self, collagenase: Collagenase):
        #comming soon
        pass
    
    def update(self, collagenase: Collagenase):
        #comming soon
        pass

    def remove(self, collagenase: Collagenase):
        #comming soon
        pass
    
    def read(self, collagenase: Collagenase):
        #comming soon
        pass
