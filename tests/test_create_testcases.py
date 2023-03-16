from pytest import mark

test_data = [('hello', 'world'),
             ('hello', ''),
             ('12345', 'world')]


@mark.parametrize('test_name, description', test_data, ids=['general test', 'test with no description', 'test with digits in name'])
def test_new_testcase(desktop_app_auth, test_name, description):
    desktop_app_auth.navigate_to('Create new test')
    desktop_app_auth.create_test(test_name, description)
    desktop_app_auth.navigate_to('Test Cases')
    test_result = desktop_app_auth.test_cases.check_testcase_exist(test_name), 'this test failed'
    desktop_app_auth.test_cases.delete_testcase_by_name(test_name)
    assert test_result
