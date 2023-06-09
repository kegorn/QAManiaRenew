import logging

from playwright.sync_api import Browser, Route, Request, ConsoleMessage, Dialog
from page_objects.test_cases_page import TestCases
from page_objects.demo_page import DemoPage

class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.page.set_default_timeout(3000)
        self.base_url = base_url
        self.test_cases = TestCases(self.page)
        self.demo_page = DemoPage(self.page)

        def console_handler(message: ConsoleMessage):
            if message.type == 'error':
                logging.error(f'page: {self.page.url}, console error: {message.text}')

        def dialog_handler(dialog: Dialog):
            logging.warning(f'page: {self.page.url}, dialog text: {dialog.message}')
            dialog.accept()

        self.page.on('console', console_handler)
        self.page.on('dialog', dialog_handler)



    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)  # "http://127.0.0.1:8000/login/?next=/"
        else:
            self.page.goto(endpoint)

    def navigate_to(self, menu: str):
        self.page.get_by_role("link", name=f"{menu}").click()
        # self.page.locator(".menuBox ")
        self.page.wait_for_load_state()

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

    def click_menu_button(self):
        self.page.locator('.menuBtn').click()

    def is_menu_button_visible(self):
        return self.page.locator('.menuBtn').is_visible()

    def get_location(self):
        return self.page.locator('.position').text_content()

    def close(self):
        self.page.close()
        self.context.close()
        # self.browser.close()

    def pause(self):
        self.page.pause()

    def intercept_requests(self, url: str, payload: str):
        def handler(route: Route, request: Request):
            route.fulfill(status=200, body=payload)

        self.page.route(url, handler)
        # yield
        # self.page.unroute(url)

    def stop_intercept(self, url: str):
        self.page.unroute(url)

    def refresh_dashboard(self):
        self.page.locator('input[value="Refresh Stats"]').click()

    def get_total_test_stats(self):
        return self.page.locator('p[class="total"] span').text_content()
