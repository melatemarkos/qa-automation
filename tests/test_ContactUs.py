'''
# ----------------------------------
Purpose: 



#-----------------------------------
'''

import pytest
import allure
import data.test_data as td
from pages.contactUs_page import ContactUsPage
from pages.home_page import HomePage


class TestContactUs:
    
    @allure.title("Test Case 6: Contact Us Form")
    def test_Contact_Us_Successfully(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        contactUs = navigate_and_verify_homepage(ContactUsPage,td.BASE_URL)

        # 4. Click on 'Contact Us' button
        contactUs.header.click_contact_us()

        # 5. Verify 'GET IN TOUCH' is visible
        assert contactUs.is_get_in_touch_header_visible()

        # 6. Enter name, email, subject and message
        contactUs.enter_name(td.CONTACT_NAME)
        contactUs.enter_email(td.CONTACT_EMAIL)
        contactUs.enter_subject(td.CONTACT_SUBJECT)
        contactUs.enter_message(td.CONTACT_MESSAGE)

        # 7. Upload file
        contactUs.upload_file(td.CONTACT_FILE_PATH)

        # 8. Click 'Submit' button
        contactUs.click_submit()

        # 9. Click OK button
        contactUs.click_okay_popup_confirmation()

        # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
        assert contactUs.is_success_message_visible()

        # 11. Click 'Home' button and verify that landed to home page successfully
        homepage = HomePage(contactUs.driver)
        homepage.header.click_home()
        assert homepage.is_logo_visible()

