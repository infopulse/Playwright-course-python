import os
from pytest import mark, fixture
from playwright.sync_api import Page, expect, BrowserContext, Browser

config = 'config.json'


@fixture(scope='session', autouse=True)
def circus(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://circus.qamania.org/')
    page.get_by_placeholder('Login').fill('a')
    page.get_by_placeholder('Password').fill('a')
    with page.expect_navigation(url='**', wait_until='networkidle'):
        page.get_by_role('button', name='Login').click()
    context.storage_state(path=config)
    page.close()
    yield context
    if os.path.exists(config):
        os.remove(config)


def test_api(circus):
    response = circus.request.get('http://circus.qamania.org/ws/performances')
    expect(response).to_be_ok()


def test_api_2(circus):
    response = circus.request.get('http://circus.qamania.org/ws/performances')
    expect(response).to_be_ok()


@mark.browser_context_args(storage_state=config)
def test_api_3(context: BrowserContext):
    response = context.request.get('http://circus.qamania.org/ws/performances')
    expect(response).to_be_ok()
