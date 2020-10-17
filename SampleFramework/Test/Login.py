import unittest

from selenium import webdriver

import allure
import pytest


@allure.story("Login Page")
@allure.feature("Login test")
class Login(unittest.TestCase):

    @allure.story("Login test")
    @allure.feature("Login with valid credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page(self):
        self.login()

    @classmethod
    @allure.step("Launch site")
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:/Program Files/PycharmProjects/pythonProject/Drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get('https://opensource-demo.orangehrmlive.com/')
        cls.driver.implicitly_wait(20)

    @allure.step("Verify Welcome message loaded")
    def login(self):
        self.driver.find_element_by_name("txtUsername").clear()
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.driver.implicitly_wait(20)
        output = self.driver.find_element_by_id("welcome").text
        print("Actual Welcome Message in the page is :",  output)
        self.assertEqual("Welcome Paul", output)

    @classmethod
    @allure.step("Browser quit")
    def tearDownClass(cls):
        cls.driver.quit()


if '__name__' == '__main__':
    unittest.main()



