from fastapi import APIRouter
from fastapi import Request

from dressings_manager_service.collagenase.application.collagenase_creator import CollagenaseCreator
from dressings_manager_service.collagenase.application.collagenase_updater import CollagenaseUpdater
from dressings_manager_service.collagenase.application.collagenase_remover import CollagenaseRemover
from dressings_manager_service.collagenase.infrastructure import item_to_collagenase_converter
from dressings_manager_service.entrypoint.items.collagenase_item import CollagenaseItem

router = APIRouter()


@router.post(
    "/collagenase",
    status_code=201,
    response_model=None,
)
def post(request: Request, collagenase: CollagenaseItem):
    collagenase = item_to_collagenase_converter.invoke(collagenase)
    collagenase_repository = request.app.collagenase_repository
    collagenase_creator = CollagenaseCreator(collagenase_repository)
    collagenase_creator.invoke(collagenase)

@router.put(
    "/collagenase",
    status_code=201,
    response_model=None,
)
def put(request: Request, collagenase: CollagenaseItem):
    collagenase = item_to_collagenase_converter.invoke(collagenase)
    collagenase_repository = request.app.collagenase_repository
    collagenase_updater = CollagenaseUpdater(collagenase_repository)
    collagenase_updater.invoke(collagenase)


@router.delete(
    "/collagenase",
    status_code=200,
    response_model=None,
)
def delete(request: Request, collagenase: CollagenaseItem):
    collagenase = item_to_collagenase_converter.invoke(collagenase)
    collagenase_repository = request.app.collagenase_repository
    collagenase_remover = CollagenaseRemover(collagenase_repository)
    collagenase_remover.invoke(collagenase) 
