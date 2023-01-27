from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('master@mail.ru')

    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_password.send_keys("98123")

    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.submit()
        time.sleep(3)
