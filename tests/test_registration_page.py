import pytest

from pages.register_page import RegisterPage


@pytest.mark.skip
def test_go_to_register(browser):
    link = 'http://34.141.58.52:8080/#/register'
    page = RegisterPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_confirm_password()
    page.go_to_button()
    browser.save_screenshot('result7.png')
