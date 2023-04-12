import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from test_python_mashroom.UI.utils import attach
from test_python_mashroom.API.utils.base_session import BaseSession
from selenium.webdriver.chrome.options import Options
import selenium

load_dotenv()


@pytest.fixture(scope="function")
def mashroom_api():
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

    browser.config.base_url = os.getenv("STEND_URL_UI")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    json_data = '{"email":"'+os.getenv("LOGIN")+'","password":"'+os.getenv("PASSWORD")+'"}'
    api_request = BaseSession((os.getenv("STEND_URL_API"))).post('/eventor/user/login', data=json_data)
    response_body = api_request.json()
    tokens = response_body.get("tokens")
    authorization_token = tokens.get("access")
    user = response_body.get("user")
    user_id = str(user.get("id"))
    user_login = user.get("login")
    user_role = user.get("role")
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
    browser.config.base_url = os.getenv("STEND_URL_USER_UI")
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()
