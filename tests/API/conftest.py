import os

import pytest
from dotenv import load_dotenv
from test_python_mashroom.API.utils.base_session import BaseSession
from selenium.webdriver.chrome.options import Options
import selenium

load_dotenv()


@pytest.fixture(scope="session")
def stend_api():
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

    return BaseSession(os.getenv('STEND_URL_API'))



