from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.__page = page
        self.__primary_header = page.locator("[data-test=\"primary-header\"]")
        self.__secondary_header = page.locator("[data-test=\"secondary-header\"]")
        self.__shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")

    def validate_primary_header_aria_snapshot(self):
        expect(self.__primary_header).to_match_aria_snapshot("- text: Swag Labs")

    def validate_secondary_header_aria_snapshot(self):
        expect(self.__secondary_header).to_match_aria_snapshot(
            "- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\"")

    def validate_shopping_cart_is_visible(self):
        expect(self.__shopping_cart_link).to_be_visible()
