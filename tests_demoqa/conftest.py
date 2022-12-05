import pytest
from selene.support.shared import browser
from selene import be, have, command


@pytest.fixture()
def open_browser():
    browser.open('https://www.google.com')
    browser.driver.set_window_size(width=1920, height=1080)
    yield




