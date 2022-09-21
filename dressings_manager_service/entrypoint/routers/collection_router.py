from fastapi import APIRouter
from fastapi import Request

from dressings_manager_service.collection.application.collection_creator import CollectionCreator
from dressings_manager_service.collection.application.collection_updater import CollectionUpdater
from dressings_manager_service.collection.application.collection_remover import CollectionRemover
from dressings_manager_service.collection.infrastructure import item_to_collection_converter
from dressings_manager_service.entrypoint.items.collection_item import CollectionItem

router = APIRouter()


@router.post(
    "/collection",
    status_code=201,
    response_model=None,
)
def post(request: Request, collection: CollectionItem):
    collection = item_to_collection_converter.invoke(collection)
    collection_repository = request.app.collection_repository
    collection_creator = CollectionCreator(collection_repository)
    collection_creator.invoke(collection)

@router.put(
    "/collection",
    status_code=201,
    response_model=None,
)
def put(request: Request, collection: CollectionItem):
    collection = item_to_collection_converter.invoke(collection)
    collection_repository = request.app.collection_repository
    collection_updater = CollectionUpdater(collection_repository)
    collection_updater.invoke(collection)


@router.delete(
    "/collection",
    status_code=200,
    response_model=None,
)
def delete(request: Request, collection: CollectionItem):
    collection = item_to_collection_converter.invoke(collection)
    collection_repository = request.app.collection_repository
    collection_remover = CollectionRemover(collection_repository)
    collection_remover.invoke(collection) 
