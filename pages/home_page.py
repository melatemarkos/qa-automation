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
from pages.header_components import HeaderComponents
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):
    
    # Locators for homepage elements
    LOGO = (By.CSS_SELECTOR, 'img[alt="Website for automation practice"]')
    SUBSCRIPTION_HEADER = (By.XPATH, "//h2[text()='Subscription']")
    SUBSCRIBE_EMAIL_INPUT = (By.ID, "susbscribe_email")
    SUBSCRIBE_BUTTON = (By.ID, "subscribe")
    SUCCESS_SUBSCRIBE_MSG = (By.ID, "success-subscribe")


    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver) 
        self.header = HeaderComponents(driver)

    def is_logo_visible(self):
        return self.is_element_visible(self.LOGO)
    
    def is_subscription_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUBSCRIPTION_HEADER))
            return True
        except TimeoutException:
            return False

    def enter_subscription_email_input(self,email):
        self.enter_text(self.SUBSCRIBE_EMAIL_INPUT,email)
        self.click(self.SUBSCRIBE_BUTTON)

    def is_subscription_success_msg_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_SUBSCRIBE_MSG))
            return True
        except TimeoutException:
            return False
        
    

    


    
