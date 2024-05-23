from pytest import mark
from playwright.sync_api import Browser


def test_users(browser: Browser):
    context1 = browser.new_context()
    context2 = browser.new_context()
    page1 = context1.new_page()
    page2 = context2.new_page()
    page1.goto('https://coffee-cart.app')
    page2.goto('https://infopulse.com')
    page3 = context1.new_page()
    page4 = context2.new_page()
    page3.goto('https://playwright.dev')
    page4.goto('https://python.org')
