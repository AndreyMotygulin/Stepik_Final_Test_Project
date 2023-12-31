from Stepik_Final_Test_Project.pages.main_page import MainPage
from Stepik_Final_Test_Project.pages.login_page import LoginPage
from Stepik_Final_Test_Project.pages.basket_page import BasketPage

import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link)
        page.open()

        page.should_be_login_link()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"

        page = MainPage(browser, link)
        page.open()

        page.should_be_basket_link()
        page.go_to_basket_page()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()

        basket_page.should_not_be_products_in_basket()
        basket_page.should_be_empty_basket_text()


