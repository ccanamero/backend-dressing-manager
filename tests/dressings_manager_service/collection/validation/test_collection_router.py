import re
from starlette.testclient import TestClient

from dressings_manager_service.entrypoint.app import app
from tests.dressings_manager_service.collection.utils import collection_mother


def test_adds_collection_to_repository(mysql_collection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collection_mother.get_collection_item().dict()
    response = client.post("/collection", json=request_body)
    saved_collection = app.collection_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(saved_collection)

def test_update_collection_to_repository(mysql_collection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collection_mother.get_collection_item().dict()
    response = client.put("/collection", json=request_body)
    updated_collection = app.collection_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(updated_collection)

def test_remove_collection_to_repository(mysql_collection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collection_mother.get_collection_item().dict()
    response = client.delete("/collection", json=request_body)
    removed_collection = app.collection_repository.retrieve(request_body["id_"])
    assert response.status_code == 200 and bool(removed_collection)