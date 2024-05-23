from pytest import mark
from playwright.sync_api import expect


def test_events_1(menu):
    menu.goto('https://coffee-cart.app/?breakable=1')
    menu.page.get_by_label('Espresso', exact=True).click()


def test_events_2(menu):
    context = menu.page.context
    with context.expect_page() as page_info:
        crt = menu.get_cart()
        crt.click(button='middle')
    page_2 = page_info.value
    assert len(context.pages) == 2
    page_2.close()
    assert len(context.pages) == 1


def test_events_3(menu):
    nah_button = menu.page.get_by_text('Nah')

    def handler():
        nah_button.click()

    menu.page.add_locator_handler(nah_button, handler)
    for i in range(10):
        menu.add_coffee('Espresso')
    expect(menu.get_total()).to_contain_text('$100.00')


def test_events_5(menu):
    nah_button = menu.page.get_by_text('Nah')
    menu.add_coffee('Espresso')
    menu.add_coffee('Espresso')
    menu.add_coffee('Espresso')
    nah_button.wait_for(state='visible')
    nah_button.click()
    nah_button.wait_for(state='hidden')
    expect(nah_button).not_to_be_visible()
