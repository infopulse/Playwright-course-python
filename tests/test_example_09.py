from pytest import mark
from playwright.sync_api import expect
from page_objects.menu import Menu


def test_coffee_1(menu):
    menu.add_coffee('Espresso')
    expect(menu.get_cart()).to_have_text('cart (1)')
    expect(menu.get_total()).to_contain_text('$10.00')
