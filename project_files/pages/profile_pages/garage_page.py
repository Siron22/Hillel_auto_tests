from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project_files.pages.base_page import BasePage

class GaragePage(BasePage):

    PAGE_TITLE_LOCATOR = (By.CSS_SELECTOR, '.panel-page_heading > h1:nth-child(1)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def page_title(self):
        return self.element(GaragePage.PAGE_TITLE_LOCATOR)
