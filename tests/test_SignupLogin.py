'''
# ----------------------------------
Purpose: 

test_SignupLogin.py contains automated test cases for verifying the signup 
and login functionality of the web application.


#-----------------------------------
'''

import pytest
import data.test_data as td
from pages.signup_login_page import SignupLoginPage
from pages.home_page import HomePage

class TestSignupLogin:
    
    # ===== Signup Tests =====
    def test_signup_new_user(self,init_driver):

        # 1. Launch browser
        signUppage = SignupLoginPage(init_driver)

        # 2. Navigate to url 'http://automationexercise.com'
        signUppage.go_to(td.BASE_URL)

        # 3. Verify that home page is visible successfully
        homepage = HomePage(init_driver)
        assert homepage.is_logo_visible()

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
    def test_login(self,init_driver):
        # 1. Launch browser
        loginpage = SignupLoginPage(init_driver)

        # 2. Navigate to url 'http://automationexercise.com'
        loginpage.go_to(td.BASE_URL)

        # 3. Verify that home page is visible successfully
        homepage = HomePage(init_driver)
        assert homepage.is_logo_visible()

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



    

