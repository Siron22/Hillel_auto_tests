import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project_files.pages.base_page import BasePage
from project_files.pages.profile_pages.garage_page import GaragePage


class RegistrationPopUp(BasePage):
    TEXT_REGISTRATION_LOCATOR = (By.CSS_SELECTOR, '.modal-title')
    FIELD_NAME_LOCATOR = (By.ID, 'signupName')
    FIELD_LAST_NAME_LOCATOR = (By.CSS_SELECTOR, '#signupLastName')
    FIELD_EMAIL_LOCATOR = (By.ID, 'signupEmail')
    FIELD_PASSWORD_LOCATOR = (By.ID, 'signupPassword')
    FIELD_REENTER_PASSWORD_LOCATOR = (By.ID, 'signupRepeatPassword')
    BUTTON_REGISTER_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(1)')
    BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')
    NAME_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='signupName']/following-sibling::div/p")
    LAST_NAME_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='signupLastName']/following-sibling::div/p")
    EMAIL_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='signupEmail']/following-sibling::div/p")
    PASSWORD_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='signupPassword']/following-sibling::div/p")
    RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR = (By.XPATH, "//input[@id='signupRepeatPassword']/following-sibling::div/p")
    USER_EXIST_ERROR_MARKER_LOCATOR = (By.CSS_SELECTOR, "p.alert")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def user_exist_error_marker(self):
        return self.element(RegistrationPopUp.USER_EXIST_ERROR_MARKER_LOCATOR)

    @property
    def name_error_marker(self):
        return self.element(RegistrationPopUp.NAME_ERROR_MARKER_LOCATOR)

    @property
    def last_name_error_marker(self):
        return self.element(RegistrationPopUp.LAST_NAME_ERROR_MARKER_LOCATOR)

    @property
    def email_error_marker(self):
        return self.element(RegistrationPopUp.EMAIL_ERROR_MARKER_LOCATOR)

    @property
    def password_error_marker(self):
        return self.element(RegistrationPopUp.PASSWORD_ERROR_MARKER_LOCATOR)

    @property
    def re_enter_password_error_marker(self):
        return self.element(RegistrationPopUp.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR)

    @property
    def text_registration(self):
        return self.element(RegistrationPopUp.TEXT_REGISTRATION_LOCATOR)

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

    @property
    def button_close(self):
        return self.element(RegistrationPopUp.BUTTON_CLOSE_LOCATOR)

    @allure.step('Enter name {name}')
    def enter_name(self, name):
        self.field_name.send_keys(name)

    @allure.step('Enter email {email}')
    def enter_email(self, email):
        self.field_email.send_keys(email)

    @allure.step('Enter lastname {lastname}')
    def enter_last_name(self, lastname):
        self.field_last_name.send_keys(lastname)

    @allure.step('Enter password {password}')
    def enter_password(self, password):
        self.field_password.send_keys(password)

    @allure.step('Renter password {password}')
    def reenter_password(self, password):
        self.field_reenter_password.send_keys(password)

    @allure.step('Click registration button')
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
        garage_page.page_title.is_displayed()
        return garage_page

    @allure.step('Click "Close" button')
    def click_close_button(self):
        self.button_close.click()