from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage
from ui_web_tests.pages.profile_pages.remove_account_pop_up import RemoveAccountPopUp


class SettingsPage(BasePage):

    INSTRUCTIONS_LOCATOR = (By.CSS_SELECTOR, '.panel-page_heading > h1:nth-child(1)')
    REMOVE_MY_ACCOUNT_LOCATOR = (By.CSS_SELECTOR, '.btn-danger-bg')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def page_title(self):
        return self.element(SettingsPage.INSTRUCTIONS_LOCATOR)

    @property
    def button_remove_my_account(self):
        return self.element(SettingsPage.REMOVE_MY_ACCOUNT_LOCATOR)


    def click_remove_my_account(self):
        self.button_remove_my_account.click()
        rem_acc = RemoveAccountPopUp(self.driver)
        return rem_acc