from pytest import fixture
from playwright.sync_api import sync_playwright

import settings
from page_objects.application import App


@fixture
def answer():
    return 42


@fixture
def new_answer(answer):
    return 42 + 1


@fixture(autouse=True, scope='function')
def pre_post_conditions():
    print('setup pre conditions')
    yield
    print('setup post conditions')


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='session')
def desktop_app(get_playwright, request):
    # base_url = request.config.getoption('--base_url')
    base_url = request.config.getini('base_url')
    app = App(get_playwright, base_url=base_url, devtools=False)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login(**settings.USER)
    yield app
    # app.close()


# hook
def pytest_addoption(parser):
    # parser.addoption('--base_url', action='store', default='http://127.0.0.1:8000')
    parser.addini('base_url', help='base url of site under test', default='http://127.0.0.1:8000')
