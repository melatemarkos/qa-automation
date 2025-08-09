'''
# ----------------------------------
Purpose: 

The home_page.py file defines the HomePage page object in the Page Object Model (POM) pattern.
 It encapsulates the behavior and elements of the websites homepage, providing reusable methods
to interact with homepage-specific features—such as verifying the visibility of the logo—abstracting 
Selenium actions for cleaner and more maintainable test code.

#-----------------------------------
'''
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    # Locators for homepage elements
    LOGO = (By.CSS_SELECTOR, 'img[alt="Website for automation practice"]')


    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver) 

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)

