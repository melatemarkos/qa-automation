'''
# ----------------------------------
Purpose: 

#-----------------------------------
'''
import os
from pages.base_page import BasePage
from pages.header_components import HeaderComponents
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ContactUsPage(BasePage):
    
    # Locators for homepage elements
    CONTACT_US_HEADER = (By.XPATH, "//h2[@class='title text-center' and contains(., 'Contact Us')]")
    GET_IN_TOUCH_HEADER = (By.XPATH, "//h2[@class='title text-center' and text()='Get In Touch']")

    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name'][data-qa='name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email'][data-qa='email']")
    SUBJECT_INPUT = (By.CSS_SELECTOR, "input[name='subject'][data-qa='subject']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea[name='message'][data-qa='message']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[name='submit'][data-qa='submit-button']")
    UPLOAD_FILE_INPUT = (By.NAME, "upload_file")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.status.alert.alert-success[style*='display: block']")


    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver) 
        self.header = HeaderComponents(driver)

    def is_get_in_touch_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_IN_TOUCH_HEADER))
            return True
        except TimeoutException:
            return False
        
    def enter_name(self,name):
        self.enter_text(self.NAME_INPUT,name)

    def enter_email(self,email):
        self.enter_text(self.EMAIL_INPUT,email)

    def enter_subject(self,subject):
        self.enter_text(self.SUBJECT_INPUT,subject)

    def enter_message(self,message):
        self.enter_text(self.MESSAGE_INPUT,message)

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def upload_file(self,file_path):
        upload = self.wait.until(EC.presence_of_element_located(self.UPLOAD_FILE_INPUT))
        upload.send_keys(file_path)

    def click_okay_popup_confirmation(self):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("No pop-up confirmation appeared to click OK")

    def is_success_message_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
            return True
        except TimeoutException:
            return False