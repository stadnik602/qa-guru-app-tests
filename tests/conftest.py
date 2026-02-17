import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_setup():
    browser.config.headless = False
    browser.config.browser_name = 'chrome'
    browser.config.window_width = '1920'

    yield

    browser.quit()