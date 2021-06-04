import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help='Choose text language for this page')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart browser")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser")
    browser.quit()


