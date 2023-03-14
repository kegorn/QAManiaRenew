class TestMyClass:
    def setup(self):
        print('Setup method nello')

    def test_new_testcase(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_testcase_exist(test_name)
        desktop_app_auth.test_cases.delete_testcase_by_name(test_name)

    def test_new_testcase_no_description(self, desktop_app_auth):
        test_name = 'hello'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, '')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_testcase_exist(test_name)
        desktop_app_auth.test_cases.delete_testcase_by_name(test_name)

    def test_new_testcase_digits_name(self, desktop_app_auth):
        test_name = '12345'
        desktop_app_auth.navigate_to('Create new test')
        desktop_app_auth.create_test(test_name, 'world')
        desktop_app_auth.navigate_to('Test Cases')
        assert desktop_app_auth.test_cases.check_testcase_exist(test_name)
        desktop_app_auth.test_cases.delete_testcase_by_name(test_name)

    def teardown(self):
        print('\nTeardown method bye')

