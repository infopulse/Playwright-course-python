from pytest import mark


@mark.testomatio('@T983cacac')
def test_check_page(page):
    page.goto('https://infopulse.com')
    assert 'Infopulse' in page.title()
