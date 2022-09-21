from fastapi import APIRouter
from fastapi import Request

from dressings_manager_service.protection.application.protection_creator import ProtectionCreator
from dressings_manager_service.protection.application.protection_updater import ProtectionUpdater
from dressings_manager_service.protection.application.protection_remover import ProtectionRemover
from dressings_manager_service.protection.infrastructure import item_to_protection_converter
from dressings_manager_service.entrypoint.items.protection_item import ProtectionItem

router = APIRouter()


@router.post(
    "/protection",
    status_code=201,
    response_model=None,
)
def post(request: Request, protection: ProtectionItem):
    protection = item_to_protection_converter.invoke(protection)
    protection_repository = request.app.protection_repository
    protection_creator = ProtectionCreator(protection_repository)
    protection_creator.invoke(protection)

@router.put(
    "/protection",
    status_code=201,
    response_model=None,
)
def put(request: Request, protection: ProtectionItem):
    protection = item_to_protection_converter.invoke(protection)
    protection_repository = request.app.protection_repository
    protection_updater = ProtectionUpdater(protection_repository)
    protection_updater.invoke(protection)


@router.delete(
    "/protection",
    status_code=200,
    response_model=None,
)
def delete(request: Request, protection: ProtectionItem):
    protection = item_to_protection_converter.invoke(protection)
    protection_repository = request.app.protection_repository
    protection_remover = ProtectionRemover(protection_repository)
    protection_remover.invoke(protection) 
