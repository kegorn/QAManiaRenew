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
def desktop_app(get_playwright):
    app = App(get_playwright, base_url=settings.BASE_URL, devtools=False)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login(**settings.USER)
    yield app
    #app.close()
