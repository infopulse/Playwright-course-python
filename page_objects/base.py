import logging
from playwright.sync_api import Page, Locator, ConsoleMessage


def get_log():
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    handler = logging.FileHandler('error.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.log = get_log()

        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage):
        if msg.type.lower() in ('error', 'warning'):
            self.log.error(f'{self.page.url}: {msg.type} {msg.text}')

    def goto(self, url, **kwargs):
        self.page.goto(url, wait_until='networkidle', **kwargs)

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
