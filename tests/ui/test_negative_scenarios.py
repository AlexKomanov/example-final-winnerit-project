from allure_commons.types import AttachmentType
from playwright.sync_api import Page, expect
import utils.configs as configs
import allure

@allure.feature("Login")
@allure.story("Negative Scenarios")
@allure.title("Login With Locked User")
def test_negative_scenarios(page: Page, login_page):
    login_page.navigate_to(configs.base_url)
    login_page.login_to_application(configs.locked_out_user, configs.correct_password)
    login_page.validate_error_message("Epic sadface: Sorry, this user has been locked out.")
    login_page.validate_page_url(configs.base_url)
    allure.attach(page.screenshot(full_page=True), name="screenshot", attachment_type=AttachmentType.PNG)
    page.wait_for_timeout(2000)
