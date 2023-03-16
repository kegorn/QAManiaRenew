from playwright.sync_api import Playwright
from page_objects.test_cases_page import TestCases


class App:
    def __init__(self, playwright: Playwright, base_url: str, headless=False, devtools=False):
        self.browser = playwright.chromium.launch(headless=headless, devtools=devtools, slow_mo=200)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.set_default_timeout(3000)
        self.base_url = base_url
        self.test_cases = TestCases(self.page)

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)  # "http://127.0.0.1:8000/login/?next=/"
        else:
            self.page.goto(endpoint)

    def navigate_to(self, menu: str):
        self.page.get_by_role("link", name=f"{menu}").click()
        self.page.locator(".menuBox ")

    def login(self, username: str, password: str):
        self.page.get_by_label("Username:").click()
        self.page.get_by_label("Username:").fill(username)
        self.page.get_by_label("Password:").click()
        self.page.get_by_label("Password:").fill(password)
        self.page.get_by_role("button", name="Login").click()

    def create_test(self, test_name: str, test_description: str):
        self.page.locator("#id_name").click()
        self.page.locator("#id_name").fill(test_name)
        self.page.locator("#id_name").press("Tab")
        self.page.get_by_label("Test description").fill(test_description)
        self.page.get_by_role("button", name="Create").click()

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
