'''
# ----------------------------------
Purpose: 

test_SignupLogin.py contains automated test cases for verifying the signup 
and login functionality of the web application.


#-----------------------------------
'''

import pytest
import allure
import data.test_data as td
from pages.signup_login_page import SignupLoginPage
from pages.home_page import HomePage

class TestSignupLogin:
    
    # ===== Signup Tests =====
    @allure.title("Test Case 1: Register User")
    def test_signup_new_user(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        signUppage = navigate_and_verify_homepage(SignupLoginPage,td.BASE_URL)

        # 4. Click on 'Signup / Login' button
        signUppage.header.click_signup_login()

        # 5. Verify 'New User Signup!' is visible
        assert signUppage.is_signup_header_visible()

        # 6. Enter name and email address
        signUppage.enter_name(td.NEW_USER_NAME)
        signUppage.enter_signup_email(td.NEW_USER_EMAIL)

        # 7. Click 'Signup' button
        signUppage.click_signup()

        # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
        assert signUppage.is_enter_account_info_visible()

        # 9. Fill details: Title, Name, Email, Password, Date of birth
        signUppage.click_titles(td.TITLE)
        signUppage.enter_name(td.NEW_USER_NAME)
        signUppage.enter_signup_password(td.NEW_PASSWORD)
        signUppage.enter_DOB(*td.DOB)

        # 10. Select checkbox 'Sign up for our newsletter!'
        signUppage.click_signup_newsletter()

        # 11. Select checkbox 'Receive special offers from our partners!'
        signUppage.click_special_offers()
        
        '''
        12. Fill details: First name, Last name, Company, 
            Address, Address2, Country, State, City, Zipcode, Mobile Number
        '''
        signUppage.enter_firstname(td.FIRSTNAME)
        signUppage.enter_lastname(td.LASTNAME)
        signUppage.enter_company(td.COMPANY)
        signUppage.enter_address_line_1(td.ADDRESS)
        signUppage.enter_country(td.COUNTRY)
        signUppage.enter_state(td.STATE)
        signUppage.enter_city(td.CITY)
        signUppage.enter_zipcode(td.ZIPCODE)
        signUppage.enter_mobile_num(td.PHONE_NUMBER)

        # 13. Click 'Create Account button'
        signUppage.click_create_acc()

        # 14. Verify that 'ACCOUNT CREATED!' is visible
        assert signUppage.is_account_created_message_visible()

        # 15. Click 'Continue' button
        signUppage.click_continue()

        # 16. Verify that 'Logged in as username' is visible
        assert signUppage.is_login_successful()

        # 17. Click 'Delete Account' button
        signUppage.click_delete_account()

        # 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
        assert signUppage.is_account_deleted()

     # ===== Login Tests =====

    @allure.title("Test Case 2: Login User with correct email and password")
    def test_login_valid_user(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        loginpage = navigate_and_verify_homepage(SignupLoginPage,td.BASE_URL)

        # 4. Click on 'Signup / Login' button
        loginpage.header.click_signup_login()

        # 5. Verify 'Login to your account' is visible
        assert loginpage.is_login_header_visible()

        # 6. Enter correct email address and password
        loginpage.enter_login_email(td.VALID_EMAIL)
        loginpage.enter_login_password(td.VALID_PASSWORD)

        # 7. Click 'login' button
        loginpage.click_login()

        # 8. Verify that 'Logged in as username' is visible
        assert loginpage.is_login_successful(td.VALID_NAME)

    @allure.title("Test Case 3: Login User with incorrect email and password")
    def test_login_invalid_user(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        loginpage = navigate_and_verify_homepage(SignupLoginPage,td.BASE_URL)

        # 4. Click on 'Signup / Login' header button
        loginpage.header.click_signup_login()

        # 5. Verify 'Login to your account' is visible
        assert loginpage.is_login_header_visible()

        # 6. Enter incorrect email address and password
        loginpage.enter_login_email(td.INVALID_EMAIL)
        loginpage.enter_login_password(td.INVALID_PASSWORD)

        # 7. Click 'login' button
        loginpage.click_login()

        # 8. Verify error 'Your email or password is incorrect!' is visible
        assert loginpage.is_invalid_entry_error_message_visible()

    @allure.title("Test Case 4: Logout User")
    def test_logout_user(self,navigate_and_verify_homepage):

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        loginpage = navigate_and_verify_homepage(SignupLoginPage,td.BASE_URL)

        # 4. Click on 'Signup / Login' button
        loginpage.header.click_signup_login()

        # 5. Verify 'Login to your account' is visible
        assert loginpage.is_login_header_visible()

        # 6. Enter correct email address and password
        loginpage.enter_login_email(td.VALID_EMAIL)
        loginpage.enter_login_password(td.VALID_PASSWORD)

        # 7. Click 'login' button
        loginpage.click_login()

        # 8. Verify that 'Logged in as username' is visible
        assert loginpage.is_login_successful()

        # 9. Click 'Logout' button
        loginpage.header.click_logout()

        # 10. Verify that user is navigated to login page
        assert loginpage.is_login_header_visible()
        
    @allure.title("Test Case 5: Register User with existing email")
    def test_register_with_existing_email(self,navigate_and_verify_homepage):
        pass

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        signUp = navigate_and_verify_homepage(SignupLoginPage,td.BASE_URL)

        # 4. Click on 'Signup / Login' button
        signUp.header.click_signup_login()

        # 5. Verify 'New User Signup!' is visible
        assert signUp.is_signup_header_visible()

        # 6. Enter name and already registered email address
        signUp.enter_name(td.EXISTING_NAME)
        signUp.enter_signup_email(td.EXISTING_EMAIL)

        # 7. Click 'Signup' button
        signUp.click_signup()

        # 8. Verify error 'Email Address already exist!' is visible
        assert signUp.is_existing_email_error_message_visible()