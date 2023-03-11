from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, devtools=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://127.0.0.1:8000/login/?next=/")
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("alica")
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Create new test").click()
    page.locator("#id_name").click()
    page.locator("#id_name").fill("hello")
    page.locator("#id_name").press("Tab")
    page.get_by_label("Test description").fill("world")
    page.get_by_role("button", name="Create").click()
    page.get_by_role("link", name="Test Cases").click()

    page.goto("http://127.0.0.1:8000/tests/")

    page.locator('xpath=//td[contains(text(),"hello")]').click()

    assert page.locator('xpath=//td[contains(text(),"hello")]') is not None


    # page.get_by_role("row", name="hello ").get_by_role("button", name="Delete").click()

    page.close()
    context.close()
    browser.close()


def test_new_testcase():
    with sync_playwright() as playwright:
        run(playwright)
