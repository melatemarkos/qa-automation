'''
# ----------------------------------
Purpose: 

BasePage serves as the common parent class in the Page Object Model (POM) pattern.
It provides reusable Selenium WebDriver utility methods and setup (e.g., waits, clicks, text entry)
that can be inherited by all specific page classes to promote code reuse and maintainability.

#-----------------------------------
'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    # Constructor
    def __init__(self,driver):
        self.driver = driver # Storing the driver so you can use it in all methods
        self.wait = WebDriverWait(driver,10) 
        # WebDriverWait for 10 seconds — this will help you wait for elements (instead of failing instantly).
    
    def go_to(self, url):
        #Navigate to specific URL
        self.driver.get(url)

    def click(self, by_locator):
        # CLick an element once its visible
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.click()

    def enter_text(self,by_locator, text):
        # Clear the field and type text into an input box
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self,by_locator):
        # Return the visible text of an element
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return element.text
    
    def is_element_visible(self,by_locator):
        # Return True if the element is visible on the page.
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False
        
    def find(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
