import os

import pytest
import selenium
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from test_python_mashroom.API.utils.base_session import BaseSession

load_dotenv()


@pytest.fixture(scope="session")
def stand_api():
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
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')
    driver = selenium.webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver

    return BaseSession(os.getenv('STEND_URL_API'))
