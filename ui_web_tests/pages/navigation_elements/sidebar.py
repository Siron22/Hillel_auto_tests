import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage
from ui_web_tests.pages.main_page_elements.main_page import MainPage
from ui_web_tests.pages.user_profile.fuel_expenses_page import FuelExpensesPage
from ui_web_tests.pages.user_profile.garage_page import GaragePage
from ui_web_tests.pages.user_profile.instructions_page import InstructionsPage
from ui_web_tests.pages.user_profile.profile_page import ProfilePage
from ui_web_tests.pages.user_profile.settings_page import SettingsPage


class Sidebar(BasePage):
    BUTTON_GARAGE_LOCATOR = (By.CSS_SELECTOR, '.sidebar > a:nth-child(1)')
    BUTTON_FUEL_EXPENSES_LOCATOR = (By.CSS_SELECTOR, '.sidebar > a:nth-child(2)')
    BUTTON_INSTRUCTION_LOCATOR = (By.CSS_SELECTOR, 'a.btn-white:nth-child(3)')
    BUTTON_PROFILE_LOCATOR = (By.XPATH, '//a[@routerlink="profile"]')
    BUTTON_SETTINGS_LOCATOR = (By.XPATH, '//a[@routerlink="settings"]')
    BUTTON_LOG_OUT_LOCATOR = (By.CSS_SELECTOR, 'a.btn:nth-child(5)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def button_garage(self):
        return self.element(Sidebar.BUTTON_GARAGE_LOCATOR)

    @property
    def button_fuel_expenses(self):
        return self.element(Sidebar.BUTTON_FUEL_EXPENSES_LOCATOR)

    @property
    def button_instruction(self):
        return self.element(Sidebar.BUTTON_INSTRUCTION_LOCATOR)

    @property
    def button_profile(self):
        return self.element(Sidebar.BUTTON_PROFILE_LOCATOR)

    @property
    def button_settings(self):
        return self.element(Sidebar.BUTTON_SETTINGS_LOCATOR)

    @property
    def button_log_out(self):
        return self.element(Sidebar.BUTTON_LOG_OUT_LOCATOR)

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

    @allure.step('Click Profile button')
    def open_profile_page(self):
        self.button_profile.click()
        return ProfilePage(self.driver)

    @allure.step('Click Settings button')
    def open_settings_page(self):
        self.button_settings.click()
        return SettingsPage(self.driver)

    @allure.step('Click Garage button')
    def open_garage_page(self):
        self.button_garage.click()
        return GaragePage(self.driver)

    @allure.step('Click Log out button')
    def click_log_out(self):
        self.button_log_out.click()
        return MainPage(self.driver)