from .locators import ProfilePageLocators
from .base_page import BasePage
import time

from .locators import LoginPageLocators


class ProfilePage(BasePage):
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

    def go_to_quit_button(self):
        quit_button = self.browser.find_element(*ProfilePageLocators.QUIT_BUTTON)
        quit_button.click()
        time.sleep(3)

    def go_to_add_pet_button(self):
        add_pet_button = self.browser.find_element(*ProfilePageLocators.ADD_PET_BUTTON)
        add_pet_button.click()

    def go_to_add_pet_name(self):
        add_pet_name = self.browser.find_element(*ProfilePageLocators.ADD_PET_NAME)
        add_pet_name.send_keys("Hitman")

    def go_to_add_pet_age(self):
        add_pet_age = self.browser.find_element(*ProfilePageLocators.ADD_PET_AGE)
        add_pet_age.send_keys("3")

    def go_to_choose_pet_type(self):
        choose_pet_type = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_TYPE)
        choose_pet_type.click()

    def go_to_choose_pet_dog(self):
        choose_pet_dog = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_DOG)
        choose_pet_dog.click()

    def go_to_choose_pet_gender(self):
        choose_pet_gender = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER)
        choose_pet_gender.click()

    def go_to_choose_pet_gender_male(self):
        choose_pet_gender_male = self.browser.find_element(*ProfilePageLocators.CHOOSE_PET_GENDER_MALE)
        choose_pet_gender_male.click()

    def go_to_submit_pet_button(self):
        submit_pet_button = self.browser.find_element(*ProfilePageLocators.SUBMIT_PET_BUTTON)
        submit_pet_button.click()
        time.sleep(2)

    def go_to_delete_pet_button(self):
        delete_pet_button = self.browser.find_element(*ProfilePageLocators.DELETE_PET_BUTTON)
        delete_pet_button.click()
        time.sleep(3)

    def go_to_no_delete_pet(self):
        no_delete_pet = self.browser.find_element(*ProfilePageLocators.NO_DELETE_PET)
        no_delete_pet.click()

    def go_to_logo_button(self):
        logo_button = self.browser.find_element(*ProfilePageLocators.LOGO)
        logo_button.click()
        time.sleep(2)

    def go_to_edit_pet_button(self):
        edit_pet_button = self.browser.find_element(*ProfilePageLocators.EDIT_PET_BUTTON)
        edit_pet_button.click()

    def go_to_edit_pet_name(self):
        edit_pet_name = self.browser.find_element(*ProfilePageLocators.EDIT_PET_NAME)
        edit_pet_name.send_keys("Maximus")

    def go_to_edit_pet_save_button(self):
        edit_pet_save_button = self.browser.find_element(*ProfilePageLocators.EDIT_PET_SAVE_BUTTON)
        edit_pet_save_button.click()
        time.sleep(3)
