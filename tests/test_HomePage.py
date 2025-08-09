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