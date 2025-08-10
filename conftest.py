'''
# ----------------------------------
Purpose: 

conftest.py is a special configuration file used by pytest to define fixtures, 
hooks, and setup/teardown code that can be shared across multiple test files in a directory or project. 
Its main purpose is to provide reusable components and configuration for tests, helping keep test code 
organized, maintainable, and DRY (Don't Repeat Yourself).
#-----------------------------------
'''

import pytest # Gives you access to the @pytest.fixture decorator.
from selenium import webdriver  #From Selenium, used to control the browser.
from selenium.webdriver.chrome.service import Service # Helps manage the ChromeDriver executable.
from webdriver_manager.chrome import ChromeDriverManager # Automatically downloads and manages the correct version of ChromeDriver for you.

from pages.signup_login_page import SignupLoginPage
from pages.home_page import HomePage
import data.test_data as td

@pytest.fixture
def init_driver():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def navigate_and_verify_homepage(init_driver):
    def _navigate(page_class,base_url):
        # Create the page object dynamically
        page = page_class (init_driver)
        page.go_to(base_url)

        # Verify home page logo is visible
        homepage = HomePage(init_driver)
        assert homepage.is_logo_visible()
        return page
    return _navigate
