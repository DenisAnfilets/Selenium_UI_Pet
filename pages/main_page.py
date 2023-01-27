
from .locators import MainPageLocators
from .base_page import BasePage
import time


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_by_type(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by_type.click()
        time.sleep(2)

    def go_to_filter_by_type_reptile(self):
        filter_by_type_reptile = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE_REPTILE)
        filter_by_type_reptile.click()
        time.sleep(3)

    def go_to_filter_by_pet_name(self):
        filter_by_pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        filter_by_pet_name.send_keys("max")

    def go_to_logo(self):
        logo = self.browser.find_element(*MainPageLocators.LOGO)
        logo.click()
        time.sleep(3)

    def go_to_like_pet(self):
        like_pet = self.browser.find_element(*MainPageLocators.LIKE_PET)
        like_pet.click()
        time.sleep(2)

    def go_to_pet_details(self):
        pet_details = self.browser.find_element(*MainPageLocators.PET_DETAILS)
        pet_details.click()
        time.sleep(3)
