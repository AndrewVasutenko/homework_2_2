from selene.support.shared import browser
from selene import be, have
import pytest


@pytest.fixture(scope="session", autouse=True)
def default_browser_resolution():
    browser.config.window_width = 800
    browser.config.window_height = 1440


def positive_search_test():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def negative_search_test():
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('njaldkasnldjnaldxal').press_enter()
    browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
