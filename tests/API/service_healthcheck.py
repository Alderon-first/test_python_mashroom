from pytest_voluptuous import S

from test_python_mashroom.API.schemas.user import create_user_schema


def test_viewer_healthcheck(example_api):
    response = example_api.get("/viewer/health")
    assert response.status_code == 200
    assert True == response.json().get("ок")
    '''
        тут json сождержит "ok": true - тоже не понятно, как проверить
    '''


def test_chat_healthcheck(example_api):
    response = example_api.get("chat/healthcheck")
    assert response.status_code == 200
    assert "true" == response.json()
    '''
    тут json сождержит только  true без заголовка - не понимаю, как провреить
    '''


def test_eventor_healthcheck(example_api):
    response = example_api.get("/eventor/health")
    assert response.status_code == 200
    assert "OK" == response.json().get("DB")
    assert "OK" == response.json().get("eventor")

