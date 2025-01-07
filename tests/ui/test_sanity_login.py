import allure
from playwright.sync_api import Page, expect
import utils.configs as configs


@allure.feature("Login")
@allure.story("Happy Scenarios")
def test_sanity_login(page: Page, login_page, products_page):

    # Login Page
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(configs.standard_user, configs.correct_password)

    # Products Page
    products_page.validate_primary_header_aria_snapshot()
    products_page.validate_secondary_header_aria_snapshot()
    products_page.validate_shopping_cart_is_visible()
    products_page.validate_page_url(configs.products_url)
    page.wait_for_timeout(2000)
