import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage
from ui_web_tests.pages.user_profile.fuel_expenses_page import FuelExpensesPage
from ui_web_tests.pages.user_profile.garage_page import GaragePage
from ui_web_tests.pages.user_profile.instructions_page import InstructionsPage


class Header(BasePage):
    BUTTON_GARAGE_LOCATOR = (By.CSS_SELECTOR, 'a.header-link:nth-child(1)')
    BUTTON_FUEL_EXPENSES_LOCATOR = (By.CSS_SELECTOR, 'a.header-link:nth-child(2)')
    BUTTON_INSTRUCTION_LOCATOR = (By.CSS_SELECTOR, 'a.header-link:nth-child(3)')
    DROPDOWN_MY_PROFILE_LOCATOR = (By.ID, 'userNavDropdown')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def button_garage(self):
        return self.element(Header.BUTTON_GARAGE_LOCATOR)

    @property
    def button_fuel_expenses(self):
        return self.element(Header.BUTTON_FUEL_EXPENSES_LOCATOR)

    @property
    def button_instruction(self):
        return self.element(Header.BUTTON_INSTRUCTION_LOCATOR)

    @property
    def dropdown_my_profile(self):
        return self.element(Header.DROPDOWN_MY_PROFILE_LOCATOR)

    @allure.step('Click garage page button')
    def open_garage_page(self):
        self.button_garage.click()
        return GaragePage(self.driver)

    @allure.step('Click Fuel expenses button')
    def open_fuel_expenses_page(self):
        self.button_fuel_expenses.click()
        return FuelExpensesPage(self.driver)

    @allure.step('Click Instruction button')
    def open_instructions_page(self):
        self.button_instruction.click()
        return InstructionsPage(self.driver)