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
from webdriver_manager.chrome import ChromeDriverManager
# Automatically downloads and manages the correct version of ChromeDriver for you.

@pytest.fixture
def init_driver():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

