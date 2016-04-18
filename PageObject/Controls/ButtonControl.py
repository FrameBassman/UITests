from selenium.webdriver.support.ui import WebDriverWait

class ButtonControl(object):
    """Base page class that is initialized on every page object class."""

    def click(self, obj):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_xpath(self.locator))
        driver.find_element_by_xpath(self.locator).click()