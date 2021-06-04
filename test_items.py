import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_language(browser):
    browser.get(link)
    button_search = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button_search
    time.sleep(1)
