'''
# ----------------------------------
Purpose: 



#-----------------------------------
'''

import pytest
import allure
import data.test_data as td
from pages.product_page import ProductPage


class TestProductPage:

    @allure.title("Test Case 8: Verify All Products and product detail page")
    def test_verify_all_products_and_details(self,navigate_and_verify_homepage):
        
        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        productPage = navigate_and_verify_homepage(ProductPage,td.BASE_URL)
    
        # 4. Click on 'Products' button
        productPage.header.click_products()

        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        assert productPage.is_product_page_header_visible()

        # 6. The products list is visible
        assert productPage.is_product_list_visible()
        assert productPage.get_products_count()

        # 7. Click on 'View Product' of first product
        productPage.click_view_first_product()

        # 8. User is landed to product detail page
        assert productPage.is_product_details_page_visible()

        # 9. Verify that details are visible: product name, category, price, availability, condition, brand
        assert productPage.are_product_details_visible()

    @allure.title("Test Case 9: Search Product")
    def test_search_product(self,navigate_and_verify_homepage):

        # 1. Launch browser
        # 2. Navigate to url 'http://automationexercise.com'
        # 3. Verify that home page is visible successfully
        productPage = navigate_and_verify_homepage(ProductPage,td.BASE_URL)

        # 4. Click on 'Products' button
        productPage.header.click_products()

        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        productPage.is_product_page_header_visible()

        # 6. Enter product name in search input and click search button
        productPage.enter_search_criteria(td.SEARCH_CRITERIA_PRODUCT_NAME)

        # 7. Verify 'SEARCHED PRODUCTS' is visible
        productPage.is_search_result_header_visible()

        # 8. Verify all the products related to search are visible
        assert productPage.is_searched_result_name_visible(td.SEARCH_CRITERIA_PRODUCT_NAME)

       
