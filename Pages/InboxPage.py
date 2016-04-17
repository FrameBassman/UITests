from PageObject.TextboxControl import BasePageElement
from PageObject.Page import BasePage
from PageObject.ButtonControl import ButtonControl
from PageObject.EmailFieldControl import EmailFieldControl
from PageObject.Locators import LogoutLocators
from PageObject.Locators import EmailLocators

class ComposeMailElement(ButtonControl):
    locator = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div'

class ToElement(EmailFieldControl):
    locator = '//textarea[@name="to"]'

class SubjectElement(EmailFieldControl):
    locator = '//input[@name="subjectbox"]'

class BodyElement(EmailFieldControl):
    locator = '//div[@aria-label="Message Body"]'

class SendElement(ButtonControl):
    locator = '//div[text()="Send"]'

class EmailSubj(BasePageElement):
    locator = '//div[5]/div/div/table/tbody/tr[1]'

class EmailRow(ButtonControl):
    locator = '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[7]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[6]/div/div/div/span[1]/b'

class InboxPage(BasePage):
    url = 'https://mail.google.com/mail/u/0/?tab=wm#inbox'

    composeMailElement = ComposeMailElement()
    toElement = ToElement()
    subjectElement = SubjectElement()
    bodyElement = BodyElement()
    sendElement = SendElement()

    emailSubj = EmailSubj()
    emailRow = EmailRow()

    def sendEmail(self, reciverEmail):
        self.driver.get(self.url)
        self.composeMailElement.click(self)
        self.toElement = reciverEmail
        self.subjectElement = 'Test'
        self.bodyElement = 'Test body'
        self.sendElement.click(self)

    def logout(self):
        element = self.driver.find_element(*LogoutLocators.FLYOUTMENU)
        element.click()
        element = self.driver.find_element(*LogoutLocators.SIGNOUT)
        element.click()
        element = self.driver.find_element(*LogoutLocators.ACCOUNTCHOOSER)
        element.click()
        element = self.driver.find_element(*LogoutLocators.ADDACCOUNT)
        element.click()

    def verifyEmail(self, body, subject):
        # self.emailRow.click(self)
        sourceSubject = self.driver.find_element(*EmailLocators.SUBJ).text
        sourceBody = self.driver.find_element(*EmailLocators.BODY).text

        assert sourceSubject.lower() == subject.lower(), 'SourceSubject is not match'
        assert sourceBody.lower() == body.lower(), 'SourceBody is not match'