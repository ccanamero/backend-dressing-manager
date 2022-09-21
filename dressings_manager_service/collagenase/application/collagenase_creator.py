from dressings_manager_service.collagenase.domain.collagenase import Collagenase
from dressings_manager_service.collagenase.domain.collagenase_repository import CollagenaseRepository


class CollagenaseCreator:
    def __init__(self, collagenase_repository: CollagenaseRepository):
        self.collagenase_repository = collagenase_repository

    def invoke(self, collagenase: Collagenase):
        self.collagenase_repository.store(collagenase)
