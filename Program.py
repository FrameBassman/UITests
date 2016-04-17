import unittest

from selenium import webdriver

from Pages import LoginPage
from Pages import InboxPage


class SendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):

            loginPage = LoginPage.LoginPage(self.driver)
            inboxPage = InboxPage.InboxPage(self.driver)

            loginPage.login('', '')
            inboxPage.sendEmail('framebassman@gmail.com')
            inboxPage.logout()
            loginPage.login('', '', True)
            inboxPage.verifyEmail(" - Test body", "Test")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()