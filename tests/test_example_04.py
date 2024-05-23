from pytest import mark


def test_check_page(page):
    page.goto('https://infopulse.com')
    assert 'Infopulse' in page.title()
