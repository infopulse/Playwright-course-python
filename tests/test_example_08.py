from pytest import mark
from playwright.sync_api import Page, expect


def test_selectors(page: Page):
    page.goto('https://coffee-cart.app/')
    espresso = page.locator('css=[data-test="Espresso"]')
    capuccino = page.locator('[data-test="Cappuccino"]')
    americano = page.locator('//div[@aria-label="Americano"]')
    expect(espresso).to_be_visible()
    expect(capuccino).to_be_visible()
    expect(americano).to_be_visible()


def test_tips_1(page: Page):
    page.goto('https://coffee-cart.app/')
    li_items = page.locator('li')
    syrup = page.locator('.syrup')
    mocha = li_items.filter(has=syrup)
    expect(mocha).to_contain_text('mocha', ignore_case=True)


def test_tips_2(page: Page):
    page.goto('https://coffee-cart.app/')
    cafe = page.get_by_label('Cafe')
    expect(cafe).to_have_count(2)
    late = page.get_by_label('Cafe').and_(page.get_by_label('Latte'))
    expect(late).to_have_count(1)
    late_not_masala = page.get_by_label(
        'Masala').or_(page.get_by_label('Latte'))
    expect(late_not_masala).to_have_count(1)


def test_tips_3(page: Page):
    page.goto('https://coffee-cart.app/')
    page.get_by_label('Espresso', exact=True).click()
    page.goto('https://coffee-cart.app/', wait_until='networkidle')
    page.wait_for_url('https://coffee-cart.app/', timeout=1000)
    page.wait_for_selector('css=[data-test="Espresso"]', timeout=1000)
    expect(page.get_by_label('Cart page')).to_contain_text('cart (0)')
