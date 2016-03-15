import unittest
from Pages import Page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SendEmail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
            #Load the main page. In this case the home page of Python.org.
            main_page = Page.MainPage(self.driver)
            #Checks if the word "Python" is in title
            assert main_page.is_title_matches(), "python.org title doesn't match."
            #Sets the text of search textbox to "pycon"
            main_page.search_text_element = "pycon"
            main_page.click_go_button()
            search_results_page = Page.SearchResultsPage(self.driver)
            #Verifies that the results page is not empty
            assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()