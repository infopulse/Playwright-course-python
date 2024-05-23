from playwright.sync_api import expect
from page_objects.menu import Menu
from pytest import mark

coffee_list = [('Espresso', '$10.00'), ('Espresso Macchiato', '$12.00'), ('Cappuccino', '$19.00'), ('Mocha', '$8.00'),
               ('Flat White',
                '$18.00'), ('Americano', '$7.00'), ('Cafe Latte', '$16.00'), ('Espresso Con Panna', '$14.00'),
               ('Cafe Breve', '$15.00')]


@mark.smoke
@mark.parametrize('coffee,price', coffee_list, ids=[f'{x[0]}-{x[1]}' for x in coffee_list])
def test_coffee_1(menu, coffee, price):
    menu.add_coffee(coffee)
    expect(menu.get_cart()).to_have_text('cart (1)')
    expect(menu.get_total()).to_contain_text(price)
