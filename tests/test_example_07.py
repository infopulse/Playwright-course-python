from pytest import mark
from playwright.sync_api import Page, expect


def test_get_method_example(page: Page):
    page.goto('https://coffee-cart.app/')
    espresso = page.get_by_label('Espresso', exact=True)
    espresso.click()
    expect(espresso).to_have_count(1)
    expect(page.get_by_label('Cart page')).to_contain_text('cart (1)')


@mark.smoke
def test_locator_features_1(page: Page):
    page.goto('https://coffee-cart.app/')
    whisky = page.get_by_label('Whisky', exact=True)
    expect(whisky).not_to_be_visible()
    assert whisky.is_visible() == False


def test_locator_features_2(page: Page):
    page.goto('https://coffee-cart.app/')
    espresso = page.get_by_label('Espresso')
    expect(espresso).to_have_count(3)


def test_locator_features_3(page: Page):
    page.goto('https://coffee-cart.app/')
    espresso = page.get_by_label('Espresso')
    espresso.first.click()
    expect(page.get_by_label('Cart page')).to_contain_text('cart (1)')
