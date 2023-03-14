def test_new_testcase(desktop_app_auth):
    test_name = 'hello'
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(test_name, 'world')
    desktop_app_auth.navigate_to('Test Cases')
    test_result = desktop_app_auth.test_cases.check_testcase_exist(test_name), 'this test failed'
    desktop_app_auth.test_cases.delete_testcase_by_name(test_name)
    assert test_result


def test_new_testcase_no_description(desktop_app_auth):
    test_name = 'hello'
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(test_name, '')
    desktop_app_auth.navigate_to('Test Cases')
    test_result = desktop_app_auth.test_cases.check_testcase_exist('failed_test')
    desktop_app_auth.test_cases.delete_testcase_by_name(test_name)
    assert test_result, 'this test failed'


def test_new_testcase_digits_name(desktop_app_auth):
    test_name = '12345'
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(test_name, 'world')
    desktop_app_auth.navigate_to('Test Cases')
    test_result = desktop_app_auth.test_cases.check_testcase_exist(test_name), 'this test failed'
    desktop_app_auth.test_cases.delete_testcase_by_name(test_name)
    assert test_result

