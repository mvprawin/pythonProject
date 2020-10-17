import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Chrome('D:/Program Files/Drivers/chromedriver.exe')
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("http://www.google.com/")
        inst.driver.title

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Python")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        print(list_new)
        self.driver.implicitly_wait(30)
        self.assertEqual(6, len(list_new))

    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("jira")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("r")
        print(lists)
        self.driver.implicitly_wait(30)
        self.assertEqual(6, len(lists))

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()
