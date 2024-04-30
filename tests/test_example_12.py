from playwright.sync_api import expect

"""
When should I use intercept?
- need a shortcut in test precondition
- need to mock a network request to 3-rd party service
- verify error from the BE handling
- ...
"""
def test_intercept(menu):
    with menu.intercept():
        menu.goto('https://coffee-cart.app/')
    # menu.page.pause()
    menu.add_coffee("Irish Coffee")
    expect(menu.get_total()).to_contain_text("$20.00")
    menu.page.reload()
    menu.add_coffee("Espresso")
    expect(menu.get_total()).to_contain_text("$10.00")
    # menu.page.pause()
