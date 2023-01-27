import pytest

from tests.test_login_page import test_go_to_login
from pages.profile_page import ProfilePage


@pytest.mark.smoke
def test_go_to_quit(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    page.go_to_quit_button()
    browser.save_screenshot('result8.png')


@pytest.mark.regression
def test_go_to_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_pet_button()
    page.go_to_add_pet_name()
    page.go_to_add_pet_age()
    page.go_to_choose_pet_type()
    page.go_to_choose_pet_dog()
    page.go_to_choose_pet_gender()
    page.go_to_choose_pet_gender_male()
    page.go_to_submit_pet_button()
    page.open()
    browser.save_screenshot('result9.png')


@pytest.mark.regression
def test_go_to_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_pet_button()
    page.go_to_no_delete_pet()


@pytest.mark.smoke
def test_go_to_logo_button(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_logo_button()
    browser.save_screenshot('result10.png')


@pytest.mark.regression
def test_edit_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit_pet_button()
    page.go_to_edit_pet_name()
    page.go_to_edit_pet_save_button()
    browser.save_screenshot('result11.png')
