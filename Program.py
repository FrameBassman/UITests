import unittest

from selenium import webdriver

from Pages import LoginPage
from Pages import InboxPage


class SendEmail(unittest.TestCase):
    @property
    def loginPage(self):
        return LoginPage.LoginPage(self.driver)

    @property
    def inboxPage(self):
        return InboxPage.InboxPage(self.driver)

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        self.loginPage.login('framebassman12', 'Tsunami9')
        self.inboxPage.sendEmail('framebassman123@gmail.com', 'Test', 'Test body')
        self.inboxPage.logout()
        self.loginPage.login('framebassman123', 'Tsunami10', True)
        self.inboxPage.verifyEmail('Test', 'Test body')

    def tearDown(self):
        self.inboxPage.removeAllEmails()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()