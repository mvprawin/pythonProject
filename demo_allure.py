import unittest
import pytest
import allure
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        self.launch_site()
        self.verify_site()

    @pytest.allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Chrome('D:/Program Files/Drivers/chromedriver.exe')
        self.driver.get("http://qaboy.com/")

    @pytest.allure.step("Verify Title loaded")
    def verify_site(self):
        list_new = self.driver.find_elements_by_class_name("site-description")
        self.driver.implicitly_wait(30)
        self.assertEqual(2, len(list_new))


if __name__ == '__main__':
    unittest.main()