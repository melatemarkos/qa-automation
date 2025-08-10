'''
# ----------------------------------
Purpose: 

The header_components.py file serves as the component class for the website’s header section 
in the Page Object Model (POM) pattern. It encapsulates locators and interaction methods 
for header elements (like navigation links, signup/login buttons, logos), enabling reusable, 
maintainable access to header functionality across tests.

#-----------------------------------
'''
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HeaderComponents(BasePage):

    # Locators for header components
    HOME_LINK = (By.CSS_SELECTOR,'a[href="/"]')
    SIGNUP_LOGIN_LINK = (By.CSS_SELECTOR,'a[href="/login"]')
    LOGOUT_LINK = (By.CSS_SELECTOR, 'a[href="/logout"]')
    PRODUCTS_LINK = (By.CSS_SELECTOR,'a[href="/products"]')
    CART_LINK = (By.CSS_SELECTOR,'a[href="/view_cart"]')
    CONTACT_US_LINK = (By.CSS_SELECTOR,'a[href="/contact_us"]')
    TEST_CASES_LINK = (By.XPATH, "//a[@href='/test_cases' and contains(text(), 'Test Cases')]")


    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver)
    
    def click_home(self):
        self.click(self.HOME_LINK)

    def click_signup_login(self):
        self.click(self.SIGNUP_LOGIN_LINK)
    
    def click_logout(self):
        self.click(self.LOGOUT_LINK)

    def click_products(self):
        self.click(self.PRODUCTS_LINK)

    def click_cart(self):
        self.click(self.CART_LINK)
    
    def click_contact_us(self):
        self.click(self.CONTACT_US_LINK)

    def click_test_cases(self):
        self.click(self.TEST_CASES_LINK)