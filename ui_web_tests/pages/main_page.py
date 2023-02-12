from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage


class MainPage(BasePage):

    LOGO_HILLEL_AUTO_LOCATOR = (By.CSS_SELECTOR, '.header_logo > svg:nth-child(1)')
    BUTTON_HOME_LOCATOR = (By.CSS_SELECTOR, 'a.btn')
    BUTTON_ABOUT_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(2)')
    BUTTON_CONTACTS_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(3)')
    BUTTON_GUEST_LOGIN_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(1)')
    BUTTON_SIGNIN_LOCATOR = (By.XPATH, '//*/div[2]/button[2]')
    BUTTON_SIGNUP_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_btn')
    STRING1_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_title') #Do more!
    STRING2_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_descr')  #With the help of ...
    VIDEO_LOCATOR = (By.CSS_SELECTOR, '.ytp-cued-thumbnail-overlay-image')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def logo_hillel_auto(self):
        return self.element(MainPage.LOGO_HILLEL_AUTO_LOCATOR)

    @property
    def button_home (self):
        return self.element(MainPage.BUTTON_HOME_LOCATOR )

    @property
    def button_about(self):
        return self.element(MainPage.BUTTON_ABOUT_LOCATOR)

    @property
    def button_contacts(self):
        return self.element(MainPage.BUTTON_CONTACTS_LOCATOR)

    @property
    def button_guest_login(self):
        return self.element(MainPage.BUTTON_GUEST_LOGIN_LOCATOR)

    @property
    def button_signin(self):
        return self.element(MainPage.BUTTON_SIGNIN_LOCATOR)

    @property
    def button_signup(self):
        return self.element(MainPage.BUTTON_SIGNUP_LOCATOR)

    @property
    def string1(self):
        return self.element(MainPage.STRING1_LOCATOR)

    @property
    def string2(self):
        return self.element(MainPage.STRING2_LOCATOR)

    @property
    def video_locator(self):
        return self.element(MainPage.VIDEO_LOCATOR)



    def click_sign_in_button(self):
        self.button_signin.click()

    def click_sign_up_button(self):
        self.button_signup.click()




