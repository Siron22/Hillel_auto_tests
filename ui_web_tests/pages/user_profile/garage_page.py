from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage

class GaragePage(BasePage):

    GARAGE_LOCATOR = (By.CSS_SELECTOR, '.panel-page_heading > h1:nth-child(1)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def garage_name(self):
        return self.element(GaragePage.GARAGE_LOCATOR)
