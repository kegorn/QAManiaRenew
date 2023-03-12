from pytest import fixture
from playwright.sync_api import sync_playwright
from page_objects.application import App


@fixture
def answer():
    return 42


@fixture
def new_answer(answer):
    return 42 + 1


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def desktop_app(get_playwright):
    app = App(get_playwright, base_url="http://127.0.0.1:8000", devtools=False)
    app.goto('/')
    yield app
    app.close()


@fixture
def desktop_app_auth(desktop_app):
    app = desktop_app
    app.goto('/login')
    app.login('alice', 'Qamania123')
    yield app

