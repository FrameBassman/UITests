import unittest
import uuid

from selenium import webdriver

from Pages import RegistrationPage


class SendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.find_element_by_css_selector()

    def test_search_in_python_org(self):
            emailAddress = str(uuid.uuid1()).replace("-", "")
            registration_page = RegistrationPage.RegistrationPage(self.driver)
            registration_page.registrate_account("UserName", emailAddress, "Debarcader12")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()