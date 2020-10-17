import unittest
from telnetlib import EC

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@allure.severity(allure.severity_level.NORMAL)
class DemoAllure(unittest.TestCase):

    def test_site_loads(self):
        self.launch_site()
        self.verify_site()

    @allure.step("Launch site")
    def launch_site(self):
        self.driver = webdriver.Chrome('D:/Program Files/Drivers/chromedriver.exe')
        self.driver.get("http://qaboy.com/")

    @allure.step("Verify Title loaded")
    def verify_site(self):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "site-title")))


if __name__ == "__main__":
    unittest.main()
