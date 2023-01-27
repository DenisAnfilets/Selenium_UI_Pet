from .base_page import BasePage
from .locators import RegisterPageLocators
import time


class RegisterPage(BasePage):
    def go_to_login(self):
        register_email = self.browser.find_element(*RegisterPageLocators.REGISTRATION_EMAIL)
        register_email.send_keys('1@mail.ru')

    def go_to_password(self):
        register_password = self.browser.find_element(*RegisterPageLocators.REGISTRATION_PASSWORD)
        register_password.send_keys("1234")

    def go_to_confirm_password(self):
        confirm_password = self.browser.find_element(*RegisterPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        confirm_password.send_keys("1234")

    def go_to_button(self):
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTRATION_BUTTON)
        register_button.submit()
        time.sleep(3)
