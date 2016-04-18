from selenium.webdriver.support.ui import WebDriverWait

class BasePageSelectElement(object):
    preElementLocator = ".//*[@id=':"
    postElementLocator = "']"

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.controlLocator))
        driver.find_element_by_xpath(self.controlLocator).click()
        driver.find_element_by_xpath(self.preElementLocator + value + self.postElementLocator).click()

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")