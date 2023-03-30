import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from test_python_mashroom.UI.utils import attach
from selenium.webdriver.chrome.options import Options
import selenium

from test_python_mashroom.API.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def stend_api():
    return BaseSession(os.getenv('STEND_URL'))


@pytest.fixture(scope="session")
def mashroom_api():
    '''
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = selenium.webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    '''
    browser.config.base_url = os.getenv("STEND_URL_UI")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    json_data = '{"email":"rebob21105@cyclesat.com","password":"123456789QWER"}'
    api_request = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/user/login', data=json_data)
    response_body = api_request.json()
    re1 = response_body.get("tokens")
    authorization_token = re1.get("access")
    re2 = response_body.get("user")
    user_id = str(re2.get("id"))
    user_login = re2.get("login")
    user_role = re2.get("role")
    browser.open('')

    browser.driver.execute_script(
        'return window.localStorage.setItem("authorization_token", "'+authorization_token+'");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_id", "' + user_id + '");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_login", "' + user_login + '");')
    browser.driver.execute_script(
        'return window.localStorage.setItem("user_role", "' + user_role + '");')
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    return browser


