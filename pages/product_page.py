'''
# ----------------------------------
Purpose: 

#-----------------------------------
'''
from pages.base_page import BasePage

class ProductPage(BasePage):
    
    # Locators for homepage elements
    


    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver) 