from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from selenium.webdriver.common.by import By


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)


