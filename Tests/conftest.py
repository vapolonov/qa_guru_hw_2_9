import pytest
from selene.support.shared import browser

@pytest.fixture(scope='session', autouse=True)
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.browser_name = 'chrome'
    browser.config.base_url = "https://demoqa.com"

@pytest.fixture()
def open_and_close_form():
    browser.open("/automation-practice-form")
    yield
    browser.element("#closeLargeModal").double_click()
    browser.close()
