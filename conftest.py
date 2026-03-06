import pytest
from playwright.sync_api import sync_playwright
from utils.config_loader import load_config

@pytest.fixture
def browser():
    config = load_config()
    with sync_playwright() as sp:
        browser = getattr(sp, config['browser']).launch(
            headless = config['headless']
        )

        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
