from Stepik_Final_Test_Project.pages.base_page import BasePage
from Stepik_Final_Test_Project.pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()

    def get_product_name(self):
        name_field = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name_field.text

    def get_product_price(self):
        price_field = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price_field.text

    def check_product_name_after_adding_to_basket(self):
        name_field_after_adding_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING)
        expected_product_name = self.get_product_name()
        actual_product_name = name_field_after_adding_to_basket.text
        assert actual_product_name == expected_product_name

    def check_product_price_after_adding_to_basket(self):
        price_field_after_adding_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_AFTER_ADDING)
        expected_product_price = self.get_product_price()
        actual_product_price = price_field_after_adding_to_basket.text
        assert actual_product_price == expected_product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_AFTER_ADDING), \
            "Success message is presented, but should be disappeared"
