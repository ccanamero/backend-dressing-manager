from dressings_manager_service.dressing.domain.dressing import Dressing
from dressings_manager_service.dressing.domain.dressing_repository import DressingRepository


class DressingCreator:
    def __init__(self, dressing_repository: DressingRepository):
        self.dressing_repository = dressing_repository

    def invoke(self, dressing: Dressing):
        self.dressing_repository.store(dressing)
