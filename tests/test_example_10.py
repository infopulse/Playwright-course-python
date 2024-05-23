from pytest import mark
import pytest


@pytest.mark.browser_context_args(locale='en-GB', geolocation={'longitude': 12.492507, 'latitude': 41.889938},
                                  permissions=['geolocation'], viewport={'width': 375, 'height': 812})
def test_browser_context_args(page):
    page.goto('/')


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args, playwright, request: pytest.FixtureRequest):
    markers = request.session.config.getoption('-m')
    if 'mobile' in markers and 'not mobile' not in markers:
        iphone_11 = playwright.devices['iPhone 11 Pro']
        return {**browser_context_args, **iphone_11}
    return browser_context_args


def test_mobile(page):
    page.goto('/')
