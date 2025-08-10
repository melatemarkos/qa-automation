import pytest
import allure
from pages.page_testcase import PageTestCase
import data.test_data as td

class TestTestCae:
    
    @allure.title("Test Case 7: Verify Test Cases Page")
    def test_verify_test_case_page(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        testcase = navigate_and_verify_homepage(PageTestCase,td.BASE_URL)

        # 4. Click on 'Test Cases' button
        testcase.header.click_test_cases()

        # 5. Verify user is navigated to test cases page successfully
        assert testcase.is_testcase_header_visible()