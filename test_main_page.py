from Stepik_Final_Test_Project.pages.main_page import MainPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)
    
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    time.sleep(5)
