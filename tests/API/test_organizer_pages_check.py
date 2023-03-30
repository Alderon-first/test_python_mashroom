import os

from dotenv import load_dotenv
from selene import have, be
from selene.support.shared import browser

from test_python_mashroom.API.utils.base_session import BaseSession

load_dotenv()
from pytest_voluptuous import S

from test_python_mashroom.API.schemas.user import create_user_schema



import requests


usernameAPI = os.getenv('usernameAuth')
passwordAPI = os.getenv('passwordAuth')
APIURL = os.getenv('APIURL')


headers = {
    "Content-Type": "application/json"
}


json_data = '{"email":"rebob21105@cyclesat.com","password":"123456789QWER"}'


def test_api_token():
    api_request = BaseSession((os.getenv("STEND_URL"))).post('/eventor/user/login', data=json_data)
    response_body = api_request.json()
    re1 = response_body.get("tokens")
    re2 = re1.get("access")
    headers = {"authorization": re2}
    request = BaseSession((os.getenv("STEND_URL"))).get('/eventor/user/181', headers=headers)
    re3 = request.json()
    print(re3)



def test_login(demoshop_api):
    demoshop_api.open('')



