from playwright.sync_api import Page, expect


class TestCases:
    def __init__(self, page: Page):
        self.page = page

    def check_testcase_exist(self, test_name: str):
        # return self.page.locator('xpath=//td[contains(text(),"hello")]')
        # return self.page.locator('css=tr').get_by_text(test_name).co
        test = self.page.query_selector(f'css=tr >> text="{test_name}"')
        return test is not None

    def delete_testcase_by_name(self, test_name: str):
        # self.page.locator("//td[text()='hello']//following::button[contains(text(), 'Delete')]").click()
        row = self.page.get_by_role('row', name=test_name).nth(00)
        row.locator('css=.deleteBtn').click()

    def check_columns_hidden(self):
        description = self.page.locator('.thDes').is_hidden()
        author = self.page.locator('.thAuthor').is_hidden()
        last_executor = self.page.locator('.thLast').is_hidden()
        return description and author and last_executor
