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
def demoshop_api():
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
    browser.config.base_url = os.getenv("STEND_URL")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    json_data = {"email": "rebob21105@cyclesat.com", "password": "123456789QWER"}
    resource = BaseSession(os.getenv("STEND_URL")).post('/eventor/user/login', data=json_data)
    authorization_cookie = resource.json()
    print(authorization_cookie)
    browser.open("")

    browser.driver.add_cookie({"name": "authorization", "value": authorization_cookie})
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    return browser


