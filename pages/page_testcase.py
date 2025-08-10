'''
# ----------------------------------
Purpose: 



#-----------------------------------
'''
from pages.base_page import BasePage
from pages.header_components import HeaderComponents
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class PageTestCase(BasePage):

    # Locators for Test Case page
    TEST_CASES_HEADER = (By.XPATH, "//b[text()='Test Cases']")
    # Constructor 
    def __init__(self,driver):
        super().__init__(driver)
        self.header = HeaderComponents(driver)

    def is_testcase_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TEST_CASES_HEADER))
            return True
        except TimeoutException:
            return False
