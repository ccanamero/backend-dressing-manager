import re
from starlette.testclient import TestClient

from dressings_manager_service.entrypoint.app import app
from tests.dressings_manager_service.protection.utils import protection_mother


def test_adds_protection_to_repository(mysql_protection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = protection_mother.get_protection_item().dict()
    response = client.post("/protection", json=request_body)
    saved_protection = app.protection_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(saved_protection)

def test_update_protection_to_repository(mysql_protection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = protection_mother.get_protection_item().dict()
    response = client.put("/protection", json=request_body)
    updated_protection = app.protection_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(updated_protection)

def test_remove_protection_to_repository(mysql_protection_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = protection_mother.get_protection_item().dict()
    response = client.delete("/protection", json=request_body)
    removed_protection = app.protection_repository.retrieve(request_body["id_"])
    assert response.status_code == 200 and bool(removed_protection)