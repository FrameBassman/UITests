from selenium.webdriver.support.ui import WebDriverWait

class BasePageSelectElement(object):

    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_class_name("goog-inline-block goog-flat-menu-button jfk-select"))
        driver.find_element_by_class_name("goog-inline-block goog-flat-menu-button jfk-select").click()

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")