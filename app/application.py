from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.support.wait import WebDriverWait
from pages.sign_in_page import SignInPage
from pages.side_menu_page import SideMenuPage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.side_menu_page = SideMenuPage(driver)
        self.sign_in_page = SignInPage(driver)
