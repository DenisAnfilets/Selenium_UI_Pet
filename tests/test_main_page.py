import pytest

from pages.main_page import MainPage


@pytest.mark.win10
@pytest.mark.regression
def test_go_to_login_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot('result5.png')


@pytest.mark.smoke
def test_filter_by_type(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    page.go_to_filter_by_type_reptile()
    browser.save_screenshot('result12.png')


@pytest.mark.xfail
def test_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    page.go_to_logo()
    browser.save_screenshot('result13.png')


@pytest.mark.smoke
def test_like_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_like_pet()
    browser.save_screenshot('result14.png')


@pytest.mark.smoke
def test_pet_details(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_pet_details()
    browser.save_screenshot('result15.png')
