import json
import allure


@allure.tag("api")
def test_viewer_healthcheck(stend_api):
    response = stend_api.get("/viewer/health")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['ok'] == True, "Значение  ok!=True"


@allure.tag("api")
@allure.feature('API')
@allure.story('Authorization')
def test_chat_healthcheck(stend_api):
    response = stend_api.get("/chat/healthcheck")
    assert response.status_code == 200
    deserialized = json.loads(response.content)
    print(deserialized)
    assert deserialized is True, "Значение в ответе !=True"


@allure.tag("api")
@allure.feature('API')
@allure.story('Authorization')
def test_poll_healthcheck(stend_api):
    response = stend_api.get("/poll/health")
    assert response.status_code == 200
    response_body = response.json()
    assert response_body['ok'] == True, "Значение  ok!=True"


@allure.tag("api")
@allure.feature('API')
@allure.story('Authorization')
def test_eventor_healthcheck(stend_api):
    response = stend_api.get("/eventor/health")
    assert response.status_code == 200
    assert "OK" == response.json().get("DB"), "Значение DB!=OK"
    assert "OK" == response.json().get("eventor"), "Значение eventor DB!=OK"
