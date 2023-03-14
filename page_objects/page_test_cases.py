from playwright.sync_api import Page


class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def check_testcase_exist(self, test_name: str):
        # return self.page.locator('xpath=//td[contains(text(),"hello")]')
        return self.page.locator('css=tr').get_by_text(test_name) is not None

    def delete_testcase_by_name(self, test_name: str):
        # self.page.locator("//td[text()='hello']//following::button[contains(text(), 'Delete')]").click()
        row = self.page.get_by_role('row', name=test_name).nth(00)
        row.locator('css=.deleteBtn').click()
