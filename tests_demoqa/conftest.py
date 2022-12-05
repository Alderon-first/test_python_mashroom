import pytest
from selene.support.shared import browser
from selene import be, have, command


@pytest.fixture()
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.set_window_size(width=1920, height=1080)
    yield




