import abc

from dressings_manager_service.collection.domain.collection import Collection


class CollectionRepository(abc.ABC):
    @abc.abstractmethod
    def store(self, collection: Collection):
        pass

    def update(self, collection: Collection):
        #comming soon
        pass

    def remove(self, collection: Collection):
        #comming soon
        pass
    
    def read(self, collection: Collection):
        #comming soon
        pass
