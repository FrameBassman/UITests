from page_objects import PageObject, page_element
from selenium import webdriver

class RegistrationPage(PageObject):
    url = 'https://accounts.google.com/SignUp?continue=https%3A%2F%2Fwww.google.ru%2F&hl=ru'

    firstName = page_element(id_='FirstName')
    lastName = page_element(id_='LastName')
    emailAddress = page_element(id_='GmailAddress')

    password = page_element(id_='Passwd')
    passwordAgain = page_element(id_='PasswdAgain')

    birthDay = page_element(id_='BirthDay')
    birthMonth = page_element(id_='BirthMonth')
    birthYear = page_element(id_='BirthYear')

    gender = page_element(id_='Gender')

    skipCaptcha = page_element(id_='SkipCaptcha')
    termsOfService = page_element(id_='TermsOfService')
    submit = page_element(id_='submitbutton')