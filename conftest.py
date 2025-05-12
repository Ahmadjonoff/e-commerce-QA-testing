from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.fixture
def page() -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-quic"])
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

@pytest.fixture
def contace_page(page):
    return ContactPage(page)