'''
# ----------------------------------
Purpose: 

#-----------------------------------
'''
from pages.base_page import BasePage
from pages.header_components import HeaderComponents
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    
    # Locators for homepage elements
    ALL_PRODUCTS_HEADER = (By.XPATH, "//h2[@class='title text-center' and text()='All Products']")
    
    PRODUCT_LIST_CONTAINER = (By.CLASS_NAME, "features_items")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .col-sm-4")
    VIEW_FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, "a[href^='/product_details/']")
    SINGLE_PRODUCT_DETAIL_HEADER = (By.CSS_SELECTOR, "div.product-information h2")
    
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product-information h2")
    CATEGORY = (By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[1]") 
    PRICE = (By.CSS_SELECTOR, "div.product-information span span")
    AVAILABILITY = (By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[2]") 
    CONDITION = (By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[3]")
    BRAND = (By.XPATH, "//section/div/div/div[2]/div[2]/div[2]/div/p[4]")

    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCH_RESULTS_HEADER = (By.XPATH, "//h2[contains(text(), 'Searched Products')]")

    SEARCH_PRODUCT_NAMES = (By.CSS_SELECTOR, ".productinfo p")



    # Constructor uses super() to OVERRIDE and use BasePage constructor 
    def __init__(self,driver):
        super().__init__(driver) 
        self.header = HeaderComponents(driver)

    def is_product_page_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS_HEADER))
            return True
        except TimeoutException:
            return False

    def is_product_list_visible(self):
        try: 
            self.wait.until(EC.visibility_of_element_located(self.PRODUCT_LIST_CONTAINER))
            return True
        except TimeoutException:
            return False
        
    def get_products_count(self):
        # Wait for the product list container to be visible first
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_LIST_CONTAINER))
        # Find all product card elements inside the container
        products = self.driver.find_elements(*self.PRODUCT_CARDS)
        return len(products)
    
    def click_view_first_product(self):
        self.click(self.VIEW_FIRST_PRODUCT_LINK)

    def is_product_details_page_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SINGLE_PRODUCT_DETAIL_HEADER))
            return True
        except TimeoutException:
            return False

    def get_product_name(self):
        return self.driver.find_element(*self.PRODUCT_NAME)
    
    def get_product_category(self):
        return self.driver.find_element(*self.CATEGORY)
    
    def get_product_price(self):
        return self.driver.find_element(*self.PRICE)
    
    def get_product_availability(self):
        return self.driver.find_element(*self.AVAILABILITY)
    
    def get_product_condition(self):
        return self.driver.find_element(*self.CONDITION)
    
    def get_product_brand(self):
        return self.driver.find_element(*self.BRAND)
    
    def are_product_details_visible(self):
      assert self.get_product_name().is_displayed()
      assert self.get_product_category().is_displayed()
      assert self.get_product_price().is_displayed()
      assert self.get_product_availability().is_displayed()
      assert self.get_product_condition().is_displayed()
      assert self.get_product_brand().is_displayed()
      return True

    def enter_search_criteria(self,criteria):
        self.enter_text(self.SEARCH_INPUT,criteria)
        self.click(self.SEARCH_BUTTON)

    def is_search_result_header_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS_HEADER))
            return True
        except TimeoutException:
            return False
        
    def get_search_name(self):
        return self.driver.find_elements(*self.SEARCH_PRODUCT_NAMES)    

    def is_searched_result_name_visible(self,criteria):
        products_name = self.get_search_name()

        if len(products_name) == 0:
            return False

        for name in products_name:
            name_text = name.text.strip().lower()
            assert criteria.lower() in name_text, f"Product '{name_text}' does not match criteria '{criteria}'"
       
        return True