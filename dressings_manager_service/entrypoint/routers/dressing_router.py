from fastapi import APIRouter
from fastapi import Request

from dressings_manager_service.dressing.application.dressing_creator import DressingCreator
from dressings_manager_service.dressing.application.dressing_updater import DressingUpdater
from dressings_manager_service.dressing.application.dressing_remover import DressingRemover
from dressings_manager_service.dressing.infrastructure import item_to_dressing_converter
from dressings_manager_service.entrypoint.items.dressing_item import DressingItem

router = APIRouter()


@router.post(
    "/dressing",
    status_code=201,
    response_model=None,
)
def post(request: Request, dressing: DressingItem):
    dressing = item_to_dressing_converter.invoke(dressing)
    dressing_repository = request.app.dressing_repository
    dressing_creator = DressingCreator(dressing_repository)
    dressing_creator.invoke(dressing)

@router.put(
    "/dressing",
    status_code=201,
    response_model=None,
)
def put(request: Request, dressing: DressingItem):
    dressing = item_to_dressing_converter.invoke(dressing)
    dressing_repository = request.app.dressing_repository
    dressing_updater = DressingUpdater(dressing_repository)
    dressing_updater.invoke(dressing)


@router.delete(
    "/dressing",
    status_code=200,
    response_model=None,
)
def delete(request: Request, dressing: DressingItem):
    dressing = item_to_dressing_converter.invoke(dressing)
    dressing_repository = request.app.dressing_repository
    dressing_remover = DressingRemover(dressing_repository)
    dressing_remover.invoke(dressing) 
