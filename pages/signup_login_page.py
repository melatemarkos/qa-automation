'''
# ----------------------------------
Purpose: 

The signup_login_page.py file represents the Signup/Login page in the Page Object Model (POM) pattern.
It encapsulates locators and methods to interact with elements related to user registration 
and login workflows, enabling clean, reusable test actions like entering user details,
 submitting forms, and verifying page behavior.

#-----------------------------------
'''

from pages.base_page import BasePage
from pages.header_components import HeaderComponents
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class SignupLoginPage(BasePage):

    # Locators for Login 

    LOGIN_EMAIL = (By.CSS_SELECTOR, 'input[data-qa="login-email"]')
    LOGIN_PASSWORD = (By.NAME,'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,'button[data-qa="login-button"]')
    LOGIN_HEADING = (By.XPATH, "//h2[text()='Login to your account']")
    LOGIN_MESSAGE = (By.XPATH, "//a[contains(.,'Logged in as')]")

    # Locators for Signup 
    NAME = (By.NAME,'name')
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    SIGNUP_PASSWORD = (By.ID,"password")
    DOB_DAY = (By.CSS_SELECTOR, 'select[data-qa="days"]')
    DOB_MONTH = (By.CSS_SELECTOR, 'select[data-qa="months"]')
    DOB_YEAR = (By.CSS_SELECTOR, 'select[data-qa="years"]')
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "optin")
    FIRST_NAME = (By.CSS_SELECTOR,'input[data-qa="first_name"]')
    LAST_NAME = (By.CSS_SELECTOR,'input[data-qa="last_name"]')
    COMPANY = (By.CSS_SELECTOR,'input[data-qa="company"]')
    ADDRESS_LINE_1 = (By.CSS_SELECTOR,'input[data-qa="address"]')
    ADDRESS_LINE_2 = (By.CSS_SELECTOR,'input[data-qa="address2"]')
    COUNTRY = (By.CSS_SELECTOR,'select[data-qa="country"]')
    STATE = (By.CSS_SELECTOR,'input[data-qa="state"]')
    CITY = (By.CSS_SELECTOR,'input[data-qa="city"]')
    ZIPCODE = (By.CSS_SELECTOR,'input[data-qa="zipcode"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR,'input[data-qa="mobile_number"]')
    CREATE_ACC_BUTTON = (By.CSS_SELECTOR,'button[data-qa="create-account"]')

    SIGNUP_EMAIL = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR,'button[data-qa="signup-button"]')
    NEW_USER_SIGNUP_HEADING = (By.XPATH, "//h2[text()='New User Signup!']")
    ENTER_ACCOUNT_INFORMATION_HEADING = (By.XPATH, "//b[normalize-space()='Enter Account Information']")
    ACCOUNT_CREATED_HEADING = (By.XPATH, "//b[normalize-space()='Account Created!']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "a[data-qa='continue-button']")
    DELETE_ACCOUNT_LINK = (By.CSS_SELECTOR, 'a[href="/delete_account"]')
    ACCOUNT_DELETED_MSG = (By.XPATH, "//b[text()='Account Deleted!']")



    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver)
        self.header = HeaderComponents(driver)

     # ===== Login Methods =====

    def is_login_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LOGIN_HEADING))
            return True
        except TimeoutException:
            return False
        
    def enter_login_email(self,email):
        self.enter_text(self.LOGIN_EMAIL,email)

    def enter_login_password(self,password):
        self.enter_text(self.LOGIN_PASSWORD,password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    
    def is_login_successful(self,username=None):
        try: 
            element = self.wait.until(EC.visibility_of_element_located(self.LOGIN_MESSAGE))
            message = element.text
            if username:
                expected = f"Logged in as {username}"
                return expected in message
            return True
        except TimeoutException:
            return False

     # ===== Signup Methods =====

    def is_signup_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.NEW_USER_SIGNUP_HEADING))
            return True
        except TimeoutException:
            return False

    def is_enter_account_info_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ENTER_ACCOUNT_INFORMATION_HEADING))
            return True
        except TimeoutException:
            return False

    def enter_name(self,name):
        self.enter_text(self.NAME,name)

    def enter_signup_email(self,email):
        self.enter_text(self.SIGNUP_EMAIL,email)

    def click_signup(self):
        self.click(self.SIGNUP_BUTTON)

    def click_titles(self,title):
        if title == 'Mr':
            self.click(self.TITLE_MR)
        elif title == 'Ms.':
            self.click(self.TITLE_MRS)
        else:
            pass # do nothing if title is not 'Mr' or 'Mrs'
    
    def enter_signup_password(self,password):
        self.enter_text(self.SIGNUP_PASSWORD,password)

    def enter_DOB(self,month,date,year):
        # Select Day
        day_dropdown = Select(self.find(self.DOB_DAY))
        day_dropdown.select_by_visible_text(str(date))

        # Select Month
        month_dropdown = Select(self.find(self.DOB_MONTH))
        month_dropdown.select_by_visible_text(str(month))

        # Select Year
        year_dropdown = Select(self.find(self.DOB_YEAR))
        year_dropdown.select_by_visible_text(str(year))

    def click_signup_newsletter(self):
        self.click(self.NEWSLETTER_CHECKBOX)

    def click_special_offers(self):
        self.click(self.SPECIAL_OFFERS_CHECKBOX)

    def enter_firstname(self,firstname):
        self.enter_text(self.FIRST_NAME,firstname)

    def enter_lastname(self,lastname):
        self.enter_text(self.LAST_NAME,lastname)

    def enter_company(self,company):
        self.enter_text(self.COMPANY,company)

    def enter_address_line_1(self,address1):
        self.enter_text(self.ADDRESS_LINE_1,address1)

    def enter_address_line_2(self,address2):
        self.enter_text(self.ADDRESS_LINE_2)
    
    def enter_country(self,country):
        country_dropdown = Select(self.find(self.COUNTRY))
        country_dropdown.select_by_visible_text(str(country))

    def enter_state(self,state):
        self.enter_text(self.STATE,state)

    def enter_city(self,city):
        self.enter_text(self.CITY,city)

    def enter_zipcode(self,zipcode):
        self.enter_text(self.ZIPCODE,zipcode)

    def enter_mobile_num(self,phoneNum):
        self.enter_text(self.MOBILE_NUMBER,phoneNum)

    def click_create_acc(self):
        self.click(self.CREATE_ACC_BUTTON)

    def is_account_created_message_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_CREATED_HEADING))
            return True
        except TimeoutException:
            return False
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_delete_account(self):
        self.click(self.DELETE_ACCOUNT_LINK)

    def is_account_deleted(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_DELETED_MSG))
            return True
        except TimeoutException:
            return False

    
    