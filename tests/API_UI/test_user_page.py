import os
import time

from selene.support.shared import browser
from selene import have

from test_python_mashroom.API.utils.base_session import BaseSession


def test_page_user_open(browser_user_event):
    """авторизация"""
    json_data = '{"email":"rebob21105@cyclesat.com","password":"123456789QWER"}'
    api_request = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/user/login', data=json_data)
    response_body = api_request.json()
    re1 = response_body.get("tokens")
    authorization_token = re1.get("access")
    '''создание мероприятия'''
    headers = {"authorization": authorization_token}
    json_data_activity = '{"activity":{"name":"test_py_user_page","isRegistrationEnabled":true,"isPreRegistrated":false,"isGenRegistration":false,"userID":181,"plannedStartDate":"2023-03-31T01:49:44.374Z","plannedStopDate":"2023-03-31T03:49:44.374Z","registration":{"anotherFields":[{"fieldUUID":"9fab144e-5046-452b-b2e0-fcabd218d021","name":"FirstName","isEnabledName":true,"isDisabledName":true,"isDisabledRequired":true,"isRequired":true,"isDigits":false,"isAlphabet":false,"maxLength":50},{"fieldUUID":"a4a809f3-6a83-4175-bde7-8e5a3e3aa674","name":"MiddleName","isEnabledName":false,"isDisabledName":false,"isDisabledRequired":true,"isRequired":false,"isDigits":false,"isAlphabet":false,"maxLength":50},{"fieldUUID":"ac9925a1-1ee6-4f69-a70e-50e1a751263c","name":"LastName","isEnabledName":false,"isDisabledName":false,"isDisabledRequired":true,"isRequired":false,"isDigits":false,"isAlphabet":false,"maxLength":50},{"fieldUUID":"e9014db1-7a8b-4c26-8c22-6c46927dd44e","name":"PhoneNumber","isEnabledName":false,"isDisabledName":false,"isDisabledRequired":true,"isRequired":false,"isDigits":true,"isAlphabet":false,"maxLength":20},{"fieldUUID":"66e19af6-5137-431d-b312-f58d3f318e2d","name":"Email","isEnabledName":true,"isDisabledName":true,"isDisabledRequired":true,"isRequired":true,"isDigits":false,"isAlphabet":false,"maxLength":50}],"allowedDomains":[],"universalStreamCode":"660036"}}}'
    api_request_activity = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/createactivity',
                                                                          data=json_data_activity, headers=headers)
    response_body_activity = api_request_activity.json()
    activity = response_body_activity.get('activity')
    print(activity)
    activity_id = str(activity.get('activityID'))
    hash_activity = str(activity.get('hash'))
    print(activity_id)
    '''просмотр страницы зрителя'''
    browser.open('/mid/?hash=' + hash_activity)
    time.sleep(3)
    browser.element(
        '#app > div > main > div > div > div.default-layout-section.mx-4.mx-md-6.mx-lg-10.px-lg-10 > div'). \
        should(have.text('test_py_user_page'))
    '''удаление мероприятия'''
    json_data_delete = '{"activity":{"activityID":' + activity_id + '}}'
    api_request_activity_delete = BaseSession((os.getenv("STEND_URL_API"))).delete('/eventor/deleteactivity',
                                                                                   data=json_data_delete,
                                                                                   headers=headers)
    response_body_activity_delete = api_request_activity_delete.json()
    print(response_body_activity_delete)
