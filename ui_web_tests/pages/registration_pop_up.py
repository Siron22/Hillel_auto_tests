from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.main_page import MainPage
from ui_web_tests.pages.user_profile.garage_page import GaragePage


class RegistrationPopUp(MainPage):

    TEXT_REGISTRATION_LOCATOR = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_CROSS_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')
    FIELD_NAME_LOCATOR = (By.ID, 'signupName')
    FIELD_LAST_NAME_LOCATOR = (By.ID, 'signupLastName')
    FIELD_EMAIL_LOCATOR = (By.ID, 'signupEmail')
    FIELD_PASSWORD_LOCATOR = (By.ID, 'signupPassword')
    FIELD_REENTER_PASSWORD_LOCATOR = (By.ID, 'signupRepeatPassword')
    BUTTON_REGISTER_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(1)')


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def text_registration(self):
        return self.element(RegistrationPopUp.TEXT_REGISTRATION_LOCATOR)

    @property
    def button_cross(self):
        return self.element(RegistrationPopUp.BUTTON_CROSS_LOCATOR)

    @property
    def field_email(self):
        return self.element(RegistrationPopUp.FIELD_EMAIL_LOCATOR)

    @property
    def field_password(self):
        return self.element(RegistrationPopUp.FIELD_PASSWORD_LOCATOR)

    @property
    def field_reenter_password(self):
        return self.element(RegistrationPopUp.FIELD_REENTER_PASSWORD_LOCATOR)

    @property
    def field_name(self):
        return self.element(RegistrationPopUp.FIELD_NAME_LOCATOR)

    @property
    def field_last_name(self):
        return self.element(RegistrationPopUp.FIELD_LAST_NAME_LOCATOR)

    @property
    def button_register(self):
        return self.element(RegistrationPopUp.BUTTON_REGISTER_LOCATOR)

    def go_to_page(self):
        self.navigate()
        self.click_sign_up_button()

    def enter_name(self, name):
        self.field_name.send_keys(name)

    def enter_email(self, email):
        self.field_email.send_keys(email)

    def enter_last_name(self, last_name):
        self.field_last_name.send_keys(last_name)

    def enter_password(self, password):
        self.field_password.send_keys(password)

    def reenter_password(self, password):
        self.field_reenter_password.send_keys(password)

    def click_registration_button(self):
        self.button_register.click()

    def _fill_registration_form_and_click_register_button(self, name, lastname, email, password):
        self.enter_name(name)
        self.enter_last_name(lastname)
        self.enter_email(email)
        self.enter_password(password)
        self.reenter_password(password)
        self.click_registration_button()

    def successful_registration(self, name, lastname, email, password):
        self._fill_registration_form_and_click_register_button(name, lastname, email, password)
        garage_page = GaragePage(self.driver)
        return garage_page

    






