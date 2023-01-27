# import pytest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = 'http://34.141.58.52:8080/#/login'
#
#
# @pytest.fixture(autouse=True)
# def browser():
#     browser = webdriver.Chrome()
#     yield browser
#     browser.quit()
#
#
# def input_login(browser):
#     input_1 = browser.find_element(By.ID, 'login')
#     input_1.send_keys('master@mail.ru')
#
#
# class TestLogin:
#
#     def test_input_login(self, browser):
#         browser.get(link)
#         input_login(browser)
#
#     def test_input_password(self, browser):
#         browser.get(link)
#         input_2 = browser.find_element(By.XPATH, '//*[@id="password"]/input')
#         input_2.send_keys("98123")
#
#     def test_submit_button(self, browser):
#         browser.get(link)
#         button = browser.find_element(By.CLASS_NAME, "p-button-label")
#         button.submit()
#         browser.save_screenshot('result.png')