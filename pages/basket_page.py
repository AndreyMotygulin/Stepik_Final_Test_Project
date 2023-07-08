from Stepik_Final_Test_Project.pages.base_page import BasePage
from Stepik_Final_Test_Project.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_url(self):
        handle = self.browser.current_url
        assert "basket" in handle, "Current url is not a basket url"

    def should_be_basket_header(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_HEADER), \
            "Basket header is not presented on basket page"

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_ITEM), \
            "The basket is not empty, there is at least one product item inside"

    def should_be_empty_basket_text(self):
        empty_basket_text_field = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        actual_empty_basket_text = empty_basket_text_field.text
        assert "Your basket is empty" in actual_empty_basket_text, \
            "The expected empty basket text ('Your basket is empty') is missing on the basket page"


