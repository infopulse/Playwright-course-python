from playwright.sync_api import Page, Locator


class Base:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url, **kwargs):
        self.page.goto(url, **kwargs)

    def navigate_to_menu(self) -> None:
        menu = self.page.locator('a[aria-label="Menu page"]')
        menu.click()
        self.page.locator("[href='/'].router-link-active").wait_for(state='visible')

    def navigate_to_cart(self) -> None:
        cart = self.page.locator('a[aria-label="Cart page"]')
        cart.click()
        self.page.locator("[href='/cart'].router-link-active").wait_for(state='visible')

    def get_cart(self) -> Locator:
        return self.page.get_by_role('link', name='cart')
