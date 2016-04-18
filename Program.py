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

            loginPage.login('framebassman12', 'Tsunami9')
            inboxPage.sendEmail('framebassman123@gmail.com', 'Test', 'Test body')
            inboxPage.logout()
            loginPage.login('framebassman123', 'Tsunami10', True)
            inboxPage.verifyEmail('Test', 'Test body')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()