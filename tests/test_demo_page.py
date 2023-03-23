def test_wait_more_30_sec(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.open_page_after_wait(3)
    assert desktop_app_auth.demo_page.check_wait_page()


def test_ajax_page_load(desktop_app_auth):
    count = 2
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.open_page_and_wait_ajax(count)
    assert count == desktop_app_auth.demo_page.get_ajax_responses_count()


def test_handlers(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.click_new_page_button()
    desktop_app_auth.demo_page.inject_js()
    desktop_app_auth.navigate_to('Test Cases')
    assert desktop_app_auth.test_cases.check_testcase_exist('Check new test')
