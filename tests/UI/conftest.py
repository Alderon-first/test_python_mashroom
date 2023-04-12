import os

import pytest
import selenium
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options

from test_python_mashroom.UI.utils import attach

load_dotenv()


@pytest.fixture(scope="function")
def browser_user_site():
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

    browser.config.base_url = os.getenv("STEND_URL_USER_UI")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)


@pytest.fixture(scope="function")
def browser_user_event():
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

    browser.config.base_url = os.getenv("STEND_URL_WIDGET_UI")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
