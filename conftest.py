from pytest import fixture
from playwright.sync_api import Page
from page_objects.menu import Menu


@fixture
def ultimate_answer():
    return 42


@fixture
def new_ultimate_answer(ultimate_answer):
    return ultimate_answer + 1


@fixture
def auth(page: Page) -> Page:
    page.goto('/')
    yield page


@fixture
def menu(auth: Page) -> Menu:
    yield Menu(auth)
