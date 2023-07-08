from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_AFTER_ADDING = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    PRODUCT_PRICE_AFTER_ADDING = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
