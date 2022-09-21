import re
from starlette.testclient import TestClient

from dressings_manager_service.entrypoint.app import app
from tests.dressings_manager_service.collagenase.utils import collagenase_mother


def test_adds_collagenase_to_repository(mysql_collagenase_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collagenase_mother.get_collagenase_item().dict()
    response = client.post("/collagenase", json=request_body)
    saved_collagenase = app.collagenase_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(saved_collagenase)

def test_update_collagenase_to_repository(mysql_collagenase_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collagenase_mother.get_collagenase_item().dict()
    response = client.put("/collagenase", json=request_body)
    updated_collagenase = app.collagenase_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and bool(updated_collagenase)

def test_remove_collagenase_to_repository(mysql_collagenase_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = collagenase_mother.get_collagenase_item().dict()
    response = client.delete("/collagenase", json=request_body)
    removed_collagenase = app.collagenase_repository.retrieve(request_body["id_"])
    assert response.status_code == 200 and bool(removed_collagenase)