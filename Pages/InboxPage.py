from page_objects import PageObject, page_element
from selenium import webdriver

class InboxPage(PageObject):
    url = 'https://mail.google.com/mail/?tab=wm#inbox?compose=new'

    to = page_element(id_=':ou')
    subject = page_element(id_=':oe')

    body = page_element(id_=':pj')

    sendButton = page_element(id_=':o4')