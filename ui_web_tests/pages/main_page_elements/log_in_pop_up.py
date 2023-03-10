import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.main_page_elements.registration_pop_up import RegistrationPopUp
from ui_web_tests.pages.main_page_elements.restore_access_pop_up import RestoreAccessPopUp
from ui_web_tests.pages.user_profile.garage_page import GaragePage
from ui_web_tests.pages.base_page import BasePage


class LoginPopUp(BasePage):
    TEXT_LOG_IN_LOCATOR = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_CROSS_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')
    FIELD_EMAIL_LOCATOR = (By.ID, 'signinEmail')
    FIELD_PASSWORD_LOCATOR = (By.ID, 'signinPassword')
    CHECK_BOX_REMEMBER_ME_LOCATOR = (By.ID, 'remember')
    BUTTON_FORGOT_PASSWORD_LOCATOR = (By.CSS_SELECTOR, 'button.btn-link:nth-child(2)')
    BUTTON_REGISTRATION_LOCATOR = (By.CSS_SELECTOR, 'button.btn:nth-child(1)')
    BUTTON_LOGIN_LOCATOR = (By.CSS_SELECTOR, 'button.btn-primary:nth-child(2)')
    BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def text_log_in(self):
        return self.element(LoginPopUp.TEXT_LOG_IN_LOCATOR)

    @property
    def button_cross(self):
        return self.element(LoginPopUp.BUTTON_CROSS_LOCATOR)

    @property
    def field_email(self):
        return self.element(LoginPopUp.FIELD_EMAIL_LOCATOR)

    @property
    def field_password(self):
        return self.element(LoginPopUp.FIELD_PASSWORD_LOCATOR)

    @property
    def check_box_remember_me(self):
        return self.element(LoginPopUp.CHECK_BOX_REMEMBER_ME_LOCATOR)

    @property
    def button_forgot_password(self):
        return self.element(LoginPopUp.BUTTON_FORGOT_PASSWORD_LOCATOR)

    @property
    def button_registration(self):
        return self.element(LoginPopUp.BUTTON_REGISTRATION_LOCATOR)

    @property
    def button_login(self):
        return self.element(LoginPopUp.BUTTON_LOGIN_LOCATOR)

    @property
    def button_close(self):
        return self.element(LoginPopUp.BUTTON_CLOSE_LOCATOR)

    @allure.step('Enter email {email}')
    def enter_email(self, email):
        self.field_email.send_keys(email)

    @allure.step('Enter password {password}')
    def enter_password(self, password):
        self.field_password.send_keys(password)

    @allure.step('Click login button')
    def click_login_button(self):
        self.button_login.click()

    def _fill_login_form_and_click_login_button(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def successful_login(self, email, password):
        self._fill_login_form_and_click_login_button(email, password)
        garage_page = GaragePage(self.driver)
        garage_page.page_title.is_displayed()
        return garage_page

    @allure.step('Click "Remember me check-box"')
    def remember_me_enable(self):
        return self.check_box_remember_me.click()

    @allure.step('Click registration button')
    def click_registration_button(self):
        self.button_registration.click()
        registration_pop_up = RegistrationPopUp(self.driver)
        registration_pop_up.button_register.is_displayed()
        return registration_pop_up

    @allure.step('Click "Forgot password" button')
    def click_forgot_password_button(self):
        self.button_forgot_password.click()
        restore_access_page = RestoreAccessPopUp(self.driver)
        restore_access_page.button_send.is_displayed()
        return restore_access_page

    @allure.step('Click "Close" button')
    def click_close_button(self):
        self.button_close.click()


