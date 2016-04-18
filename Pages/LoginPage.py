from PageObject.BasePageElement import BasePageElement
from PageObject.Locators import LoginPageLocators
from PageObject.Page import BasePage

class UsernameElement(BasePageElement):
    locator = 'Email'

class PasswordElement(BasePageElement):
    locator = 'Passwd'

class LoginPage(BasePage):
    url = 'https://accounts.google.com/ServiceLogin?hl=ru&passive=true&continue=https://www.google.ru/#identifier'
    urlAfterLogout = 'https://accounts.google.com/ServiceLogin?sacu=1&scc=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en-GB&service=mail#identifier'
    username_element = UsernameElement()
    password_element = PasswordElement()

    def login(self, username, password, afterLogout=False):
        if afterLogout == True:
            self.url = self.urlAfterLogout

        self.driver.get(self.url)
        self.username_element = username
        element = self.driver.find_element(*LoginPageLocators.NEXT)
        element.click()

        self.driver.implicitly_wait(10)

        self.password_element = password
        element = self.driver.find_element(*LoginPageLocators.SIGNIN)
        element.click()

