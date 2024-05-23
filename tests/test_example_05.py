from pytest import mark
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto('https://coffee-cart.app/')
    page.locator('[data-test="Espresso"]').click()
    page.locator('[data-test="Espresso_Macchiato"]').click()
    page.locator('[data-test="Cappuccino"]').click()
    page.get_by_role('button', name='Yes, of course!').click()
    expect(page.get_by_label('Cart page')).to_contain_text('cart (4)')
