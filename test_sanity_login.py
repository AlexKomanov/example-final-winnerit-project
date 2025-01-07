from playwright.sync_api import Page, expect


def test_example(page: Page):
    base_url = "https://www.saucedemo.com/"
    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.get_by_placeholder("Password").press_sequentially("secret_sauce", delay=300)
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"primary-header\"]")).to_match_aria_snapshot("- text: Swag Labs")
    expect(page.locator("[data-test=\"secondary-header\"]")).to_match_aria_snapshot("- text: Products Name (A to Z)\n- combobox:\n  - option \"Name (A to Z)\" [selected]\n  - option \"Name (Z to A)\"\n  - option \"Price (low to high)\"\n  - option \"Price (high to low)\"")
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    expect(page).to_have_url(f"{base_url}inventory.html")
    page.wait_for_timeout(2000)
