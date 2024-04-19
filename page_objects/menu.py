from page_objects.base import Base
from playwright.sync_api import Locator


class Menu(Base):
    def add_coffee(self, name: str) -> None:
        self.page.get_by_label(name, exact=True).click()

    def get_total(self) -> Locator:
        return self.page.locator('.pay')
