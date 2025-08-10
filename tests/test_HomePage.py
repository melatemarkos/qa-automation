'''
# ----------------------------------
Purpose: 

The test_HomePage.py file contains automated test cases for verifying key 
functionalities of the website’s homepage using the Page Object Model. Specifically, 
it tests whether critical elements, like the homepage logo, are visible and properly 
loaded, ensuring the page behaves as expected and maintaining the quality of the web 
application.

#-----------------------------------
'''

import pytest
import data.test_data as td
from pages.home_page import HomePage

class TestHomePage:

    def test_logo_visibility(self,init_driver):
        homepage = HomePage(init_driver)
        homepage.go_to(td.BASE_URL)
        assert homepage.is_logo_visible()

    def test_subscription(self,navigate_and_verify_homepage):

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        subscription = navigate_and_verify_homepage(HomePage,td.BASE_URL)

        # 4. Scroll down to footer
        # 5. Verify text 'SUBSCRIPTION'
        subscription.is_subscription_header_visible()

        # 6. Enter email address in input and click arrow button
        subscription.enter_subscription_email_input(td.SUBSCRIPTION_EMAIL)

        # 7. Verify success message 'You have been successfully subscribed!' is visible
        assert subscription.is_subscription_success_msg_visible()
