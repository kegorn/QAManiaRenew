def test_wait_more_30_sec(desktop_app_auth):
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.open_page_after_wait(32)
    assert desktop_app_auth.demo_page.check_wait_page()


def test_ajax_page_load(desktop_app_auth):
    count = 6
    desktop_app_auth.navigate_to('Demo pages')
    desktop_app_auth.demo_page.open_page_and_wait_ajax(count)
    assert count == desktop_app_auth.demo_page.get_ajax_responses_count()
