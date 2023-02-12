from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage


class RestoreAccessPage(BasePage):

    TEXT_RESTORE_ACCESS_LOCATOR = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_CROSS_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')
    FIELD_EMAIL_LOCATOR = (By.ID, 'signinEmail')
    BUTTON_SEND_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(1)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def text_restore(self):
        return self.element(RestoreAccessPage.TEXT_RESTORE_ACCESS_LOCATOR)

    @property
    def button_cross(self):
        return self.element(RestoreAccessPage.BUTTON_CROSS_LOCATOR)

    @property
    def field_email(self):
        return self.element(RestoreAccessPage.FIELD_EMAIL_LOCATOR)

    @property
    def button_send(self):
        return self.element(RestoreAccessPage.BUTTON_SEND_LOCATOR)

    def enter_email(self, email):
        self.field_email.send_keys(email)

    def click_send_button(self):
        self.button_send.click()

    def fill_restore_form_and_click_send_button(self, email):
        self.enter_email(email)
        self.click_send_button()
