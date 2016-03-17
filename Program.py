import unittest

from selenium import webdriver

from Pages import RegistrationPage


class SendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.find_element_by_css_selector()

    def test_search_in_python_org(self):
            registration_page = RegistrationPage.RegistrationPage(self.driver)
            registration_page.registrate_account("framebassman12", "framebassman12@gmail.com", "112312313123123")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()