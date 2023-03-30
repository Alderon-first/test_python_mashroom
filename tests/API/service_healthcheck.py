from pytest_voluptuous import S
import json
from test_python_mashroom.API.schemas.user import create_user_schema


def test_viewer_healthcheck(example_api):
    response = example_api.get("/viewer/health")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['ok'] == True


def test_chat_healthcheck(example_api):
    response = example_api.get("/chat/healthcheck")
    assert response.status_code == 200
    deserialized = json.loads(response.content)
    print(deserialized)
    assert deserialized is True


def test_eventor_healthcheck(example_api):
    response = example_api.get("/eventor/health")
    assert response.status_code == 200
    assert "OK" == response.json().get("DB"), "Значение DB!=OK"
    assert "OK" == response.json().get("eventor"), "eventor DB!=OK"
