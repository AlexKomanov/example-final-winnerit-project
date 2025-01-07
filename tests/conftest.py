import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def products_page(page: Page):
    return ProductsPage(page)