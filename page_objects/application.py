from playwright.sync_api import Playwright


class App:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, devtools=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("http://127.0.0.1:8000/login/?next=/")

    def login(self):
        self.page.get_by_label("Username:").click()
        self.page.get_by_label("Username:").fill("alice")
        self.page.get_by_label("Password:").click()
        self.page.get_by_label("Password:").fill("Qamania123")
        self.page.get_by_role("button", name="Login").click()

    def create_test(self):
        self.page.get_by_role("link", name="Create new test").click()
        self.page.locator("#id_name").click()
        self.page.locator("#id_name").fill("hello")
        self.page.locator("#id_name").press("Tab")
        self.page.get_by_label("Test description").fill("world")
        self.page.get_by_role("button", name="Create").click()

    def open_tests(self):
        self.page.get_by_role("link", name="Test Cases").click()

    def check_testcase_created(self):
        # return self.page.locator('xpath=//td[contains(text(),"hello")]')
        return True

    def delete_testcase(self):
        pass

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
