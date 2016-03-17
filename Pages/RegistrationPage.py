from PageObject.Element import BasePageElement
from PageObject.Locators import RegistrationPageLocators
from PageObject.Page import BasePage
from PageObject.SelectElement import BasePageSelectElement


#region Locators.

class FirstNameElement(BasePageElement):
    locator = 'FirstName'
class LastNameElement(BasePageElement):
    locator = 'LastName'
class EmailAddressElement(BasePageElement):
    locator = 'GmailAddress'
class PasswordElement(BasePageElement):
    locator = 'Passwd'
class PasswordAgainElement(BasePageElement):
    locator = 'PasswdAgain'
class BirthDayElement(BasePageElement):
    locator = 'BirthDay'
class BirthMonthElement(BasePageSelectElement):
    locator = 'BirthMonth'
class BirthYearElement(BasePageElement):
    locator = 'BirthYear'
class GenderElement(BasePageElement):
    locator = 'Gender'
class SkipCaptchaElement(BasePageElement):
    locator = 'SkipCaptcha'
class TermsOfServiceElement(BasePageElement):
    locator = 'TermsOfService'

#endregion

class RegistrationPage(BasePage):
    url = 'https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.com%2F&hl=en'

    first_name_element = FirstNameElement()
    last_name_element = LastNameElement()
    email_address_element = EmailAddressElement()

    password_element = PasswordElement()
    password_again_element = PasswordAgainElement()

    birth_day_element = BirthDayElement()
    birth_month_element = BirthMonthElement()
    birth_year_element = BirthYearElement()

    gender_element = GenderElement()
    skip_captcha_element = SkipCaptchaElement()
    terms_of_service_element = TermsOfServiceElement()

    def registrate_account(self, accountName, email, password):
        self.driver.get(self.url)

        self.first_name_element = accountName
        self.last_name_element = accountName
        self.email_address_element = email

        self.password_element = password
        self.password_again_element = password

        self.birth_day_element = "1"
        self.birth_month_element = "May"
        self.birth_year_element = "1990"

        element = self.driver.find_element(*RegistrationPageLocators.SUBMIT)
        element.click()