import pytest
from playwright.sync_api import sync_playwright
from config.settings import *


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        yield browser

        browser.close()

@pytest.fixture
def context(browser):

    context = browser.new_context(viewport=VIEWPORT)

    yield context

    context.close()

@pytest.fixture
def page(context):

    page = context.new_page()

    page.set_default_timeout(DEFAULT_TIMEOUT)

    yield page

    page.close()
