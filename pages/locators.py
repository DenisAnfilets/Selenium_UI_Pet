from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.XPATH, '//*[@id="typesSelector"]')
    FILTER_BY_TYPE_REPTILE = (By.XPATH, '//*[@aria-label="reptile"]')
    FILTER_BY_PET_NAME = (By.XPATH, '//*[@id="petName"]')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')
    LIKE_PET = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[2]/span[1]/i')
    PET_DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button/span')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'login')
    LOGIN_PASSWORD = (By.XPATH, '//*[@id="password"]/input')
    LOGIN_BUTTON = (By.CLASS_NAME, "p-button-label")


class RegisterPageLocators:
    REGISTRATION_EMAIL = (By.ID, 'login')
    REGISTRATION_PASSWORD = (By.XPATH, '//*[@id="password"]/input')
    REGISTRATION_CONFIRM_PASSWORD = (By.XPATH, '//*[@id="confirm_password"]/input')
    REGISTRATION_BUTTON = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    QUIT_BUTTON = (By.XPATH, '//*[@id="app"]/header/div/ul/li[2]/a/span[2]')
    ADD_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[1]/div/div[1]/button/span[1]')
    ADD_PET_NAME = (By.XPATH, '//*[@id="name"]')
    ADD_PET_AGE = (By.XPATH, '//*[@id="age"]/input')
    CHOOSE_PET_TYPE = (By.XPATH, '//*[@id="typeSelector"]')
    CHOOSE_PET_DOG = (By.XPATH, '//*[@aria-label="dog"]')
    CHOOSE_PET_GENDER = (By.ID, 'genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    SUBMIT_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]/span[2]')
    CANCEL_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[2]/span[2]')
    CHOOSE_PET_AVA_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div[2]/div/span/span[2]')
    DELETE_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[4]/div/div[2]/button[2]/span[2]')
    NO_DELETE_PET = (By.XPATH, '/html/body/div[3]/div[2]/button[1]')
    LOGO = (By.XPATH, '//*[@id="app"]/header/div/div/img')
    EDIT_PET_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]/span[2]')
    EDIT_PET_NAME = (By.XPATH, '//*[@id="name"]')
    EDIT_PET_SAVE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/form/div/div[2]/div[3]/button/span[2]')
