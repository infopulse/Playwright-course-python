from pytest import mark


@mark.testomatio('@Tb28de546')
def test_check_page(page):
    page.goto('https://infopulse.com')
    assert 'Infopulse' in page.title()
