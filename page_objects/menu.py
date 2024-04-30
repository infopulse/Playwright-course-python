from page_objects.base import Base
from playwright.sync_api import Locator, Route, Request
from contextlib import contextmanager


class Menu(Base):
    def add_coffee(self, name: str) -> None:
        self.page.get_by_label(name, exact=True).click()

    def get_total(self) -> Locator:
        return self.page.locator('.pay')

    @contextmanager
    def intercept(self):
        self.page.route(url="**/list.json", handler=Menu._intercept_handler)
        yield
        self.page.unroute(url="**/list.json")

    @staticmethod
    def _intercept_handler(route: Route, request: Request):
        route.fulfill(status=200, json=[{
            "name": "Irish Coffee",
            "price": 20,
            "recipe": [
                {"name": "espresso", "quantity": 40},
                {"name": "irish whiskey", "quantity": 15},
                {"name": "whipped cream", "quantity": 10}
            ]
        }])

    def auto_decline_extra_coffee(self) -> None:
        nah_button = self.page.get_by_text("Nah")

        def handler():
            nah_button.click()

        self.page.add_locator_handler(nah_button, handler)
