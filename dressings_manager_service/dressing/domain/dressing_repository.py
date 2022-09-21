import abc

from dressings_manager_service.dressing.domain.dressing import Dressing


class DressingRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, dressing: Dressing):
        pass

    def update(self, dressing: Dressing):
        #comming soon
        pass

    def remove(self, dressing: Dressing):
        #comming soon
        pass
    
    def read(self, dressing: Dressing):
        #comming soon
        pass