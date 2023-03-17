from pytest import fixture
from playwright.sync_api import sync_playwright
from settings import BROWSER_OPTIONS
from page_objects.application import App
import os
import json


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
    base_url = request.config.getoption('--base_url')
    # 3
    # base_url = request.config.getini('base_url')
    # 4
    # base_url = request.config.getoption('--base_url')
    app = App(get_playwright, base_url=base_url, devtools=False, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def desktop_app_auth(desktop_app):
    # secure = request.config.getoption('--secure')
    # config = load_config(secure)
    account = {'username': os.environ['USER'],
               'password': os.environ['PASSWORD']}

    app = desktop_app
    app.goto('/login')
    app.login(**account)
    yield desktop_app


@fixture(scope='session')
def mobile_app(get_playwright, request):
    base_url = request.config.getoption('--base_url')
    device = request.config.getoption('--device')
    app = App(get_playwright, base_url=base_url, devtools=False, device=device, **BROWSER_OPTIONS)
    app.goto('/')
    yield app
    app.close()


@fixture(scope='session')
def mobile_app_auth(mobile_app):
    account = {'username': os.environ['USER'],
               'password': os.environ['PASSWORD']}

    app = mobile_app
    app.goto('/login')
    app.login(**account)
    yield app



# hook
def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='http://127.0.0.1:8000')
    parser.addoption('--device', action='store', default='')
    # parser.addini('base_url', help='base url of site under test', default='http://127.0.0.1:8000')
    # 4
    # parser.addoption('--base_url', action='store', default='http://127.0.0.1:8000')
    # parser.addoption('--secure', action='store', default='secure.json')


# def load_config(file):
#     config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
#     with open(config_file) as cfg:
#         return json.loads(cfg.read())
