from playwright.sync_api import Page, expect
import allure
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__username_textfield = page.locator("[data-test=\"username\"]")
        self.__password_textfield = page.get_by_placeholder("Password")
        self.__login_button = page.get_by_role("button", name="Login")
        self.__error_message = page.locator("[data-test=\"error\"]")

    def navigate_to(self, url: str):
        with allure.step(f"Navigating to url: {url}"):
            self.__page.goto(url)


    def login_to_application(self, username: str, password: str):
        with allure.step(f"Login to app with credentials: {username} : {password}"):
            self.__username_textfield.fill(username, timeout=60000)
            self.__password_textfield.press_sequentially(password, delay=100)
            self.__login_button.click()


    def validate_error_message(self, error_message: str):
        with allure.step(f"Validating that error message is: '{error_message}'"):
            expect(self.__error_message).to_contain_text(error_message)



