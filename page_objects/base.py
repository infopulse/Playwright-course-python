import logging
import uuid
import os
from playwright.sync_api import Page, Locator, ConsoleMessage


class Base:
    def __init__(self, page: Page):
        self.page = page
        self.context = page.context

        self.page.on('console', self._console_handler)

    def _console_handler(self, msg: ConsoleMessage):
        if msg.type.lower() in ('error', 'warning'):
            pass
            # raise Exception(f'{self.page.url}: {msg.type} {msg.text}')

    def goto(self, url, **kwargs):
        self.page.goto(url, wait_until='networkidle', **kwargs)

    def navigate_to_menu(self) -> None:
        menu = self.page.locator('a[aria-label="Menu page"]')
        menu.click()
        self.page.locator("[href='/'].router-link-active").wait_for(state='visible')

    def get_cart(self) -> Locator:
        return self.page.get_by_role('link', name='cart')

    def navigate_to_cart(self, new_window=False) -> Page:
        cart = self.get_cart()
        if not new_window:
            cart.click()
            self.page.locator("[href='/cart'].router-link-active").wait_for(state='visible')
            return self.page
        else:
            with self.context.expect_page() as page_info:
                cart.click(button='middle')
            page_2 = page_info.value
            page_2.locator("[href='/cart'].router-link-active").wait_for(state='visible')
            return page_2

    def get_pages(self) -> list[Page]:
        return self.page.context.pages
