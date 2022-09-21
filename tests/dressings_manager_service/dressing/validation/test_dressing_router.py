import re
from starlette.testclient import TestClient

from dressings_manager_service.entrypoint.app import app
from tests.dressings_manager_service.dressing.utils import dressing_mother


def test_adds_dressing_to_repository(mysql_dressing_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = dressing_mother.get_dressing_item().dict()
    response = client.post("/dressing", json=request_body)
    saved_dressing = app.dressing_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(saved_dressing)

def test_update_dressing_to_repository(mysql_dressing_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = dressing_mother.get_dressing_item().dict()
    response = client.put("/dressing", json=request_body)
    updated_dressing = app.dressing_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(updated_dressing)

def test_remove_dressing_to_repository(mysql_dressing_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = dressing_mother.get_dressing_item().dict()
    response = client.delete("/dressing", json=request_body)
    removed_dressing = app.dressing_repository.retrieve(request_body["id_"])
    assert response.status_code == 200 and bool(removed_dressing)