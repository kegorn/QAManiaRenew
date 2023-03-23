from playwright.sync_api import Page


class DemoPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open_page_after_wait(self, wait_time: int):
        self.page.fill('.waitPageTime', str(wait_time))
        with self.page.expect_navigation(wait_until='load', timeout=(wait_time + 1) * 1000):
            self.page.click('.waitPage', no_wait_after=True)

    def check_wait_page(self):
        return 'Wait Page' == self.page.locator('h3').text_content()

    def open_page_and_wait_ajax(self, wait_time: int):
        self.page.locator('.waitAjaxRequests').fill(str(wait_time))
        self.page.locator('.waitAjax').click()
        self.page.wait_for_load_state('networkidle')

    def get_ajax_responses_count(self):
        return self.page.locator('p').count()

    def click_new_page_button(self, ctrl_key=False):
        if ctrl_key:
            mod = ['Control']
        else:
            mod = None
        self.page.click('.newPage', modifiers=mod)

    def inject_js(self):
        js = '''
        console.error('this is injected error');
        alert('this is injected alert');
        '''
        self.page.evaluate(js)

