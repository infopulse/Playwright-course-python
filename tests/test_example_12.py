from pytest import mark
from playwright.sync_api import expect

'\nWhen should I use intercept?\n- need a shortcut in test precondition\n- need to mock a network request to 3-rd party service\n- verify error from the BE handling\n- ...\n'


def test_intercept(menu):
    with menu.intercept():
        menu.goto('https://coffee-cart.app/')
    menu.add_coffee('Irish Coffee')
    expect(menu.get_total()).to_contain_text('$20.00')
    menu.page.reload()
    menu.add_coffee('Espresso')
    expect(menu.get_total()).to_contain_text('$10.00')
