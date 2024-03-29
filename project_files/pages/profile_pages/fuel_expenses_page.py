from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project_files.pages.base_page import BasePage

class FuelExpensesPage(BasePage):

    FUEL_EXPENSES_LOCATOR = (By.CSS_SELECTOR, '.panel-page_heading > h1:nth-child(1)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def page_title(self):
        return self.element(FuelExpensesPage.FUEL_EXPENSES_LOCATOR)

