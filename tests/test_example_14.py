from pytest import mark
from playwright.sync_api import Page, expect


@mark.smoke
def test_api(page: Page):
    response = page.request.get('/list.json')
    expect(response).to_be_ok()
    assert len(response.json()) == 10
    response = page.request.post('/list.json', data='hello world')
    expect(response).not_to_be_ok()


def test_coffee_14(menu):
    menu.add_coffee('Espresso')
    expect(menu.get_cart()).to_have_text('cart (1)')
    expect(menu.get_total()).to_contain_text('$10.00')
    response = menu.page.request.get('/list.json')
    expect(response).to_be_ok()
