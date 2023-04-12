import os
import time

from selene import have
from selene.support.shared import browser

from test_python_mashroom.API.schemas.data import json_data_activity_open
from test_python_mashroom.API.utils.base_session import BaseSession


def test_page_user_open(browser_user_event):
    """авторизация"""
    json_data = '{"email":"' + os.getenv("LOGIN") + '","password":"' + os.getenv("PASSWORD") + '"}'
    api_request = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/user/login', data=json_data)
    response_body = api_request.json()
    re1 = response_body.get("tokens")
    authorization_token = re1.get("access")
    '''создание мероприятия'''
    headers = {"authorization": authorization_token}
    json_data_activity = json_data_activity_open
    api_request_activity = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/createactivity',
                                                                          data=json_data_activity, headers=headers)
    response_body_activity = api_request_activity.json()
    activity = response_body_activity.get('activity')
    activity_id = str(activity.get('activityID'))
    hash_activity = str(activity.get('hash'))
    '''просмотр страницы зрителя'''
    browser.open('/mid/?hash=' + hash_activity)
    time.sleep(3)
    browser.element(
        '#app > div > main > div > div > div.default-layout-section.mx-4.mx-md-6.mx-lg-10.px-lg-10 > div'). \
        should(have.text('test_py_user_page'))
    '''удаление мероприятия'''
    json_data_delete = '{"activity":{"activityID":' + activity_id + '}}'
    BaseSession((os.getenv("STEND_URL_API"))).delete('/eventor/deleteactivity', data=json_data_delete, headers=headers)
