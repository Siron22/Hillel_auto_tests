import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage
from ui_web_tests.pages.main_page_elements.log_in_pop_up import LoginPopUp
from ui_web_tests.pages.main_page_elements.registration_pop_up import RegistrationPopUp


class MainPage(BasePage):
    LOGO_HILLEL_AUTO_LOCATOR = (By.CSS_SELECTOR, '.header_logo > svg:nth-child(1)')
    BUTTON_HOME_LOCATOR = (By.CSS_SELECTOR, 'a.btn')
    BUTTON_ABOUT_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(2)')
    BUTTON_CONTACTS_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(3)')
    BUTTON_GUEST_LOGIN_LOCATOR = (By.CSS_SELECTOR, 'button.header-link:nth-child(1)')
    BUTTON_SIGNIN_LOCATOR = (By.XPATH, '//*/div[2]/button[2]')
    BUTTON_SIGNUP_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_btn')
    STRING1_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_title')  # Do more!
    STRING2_LOCATOR = (By.CSS_SELECTOR, '.hero-descriptor_descr')  # With the help of ...
    VIDEO_LOCATOR = (By.CSS_SELECTOR, '.ytp-large-play-button')
    ABOUT_SECTION_LOCATOR = (By.ID, 'aboutSection')
    TEXT_CONTACTS_LOCATOR = (By.XPATH, '//h2[text()="Contacts"]')
    ICON_FACEBOOK_LOCATOR = (By.CSS_SELECTOR, '.icon-facebook')
    ICON_TELEGRAM_LOCATOR = (By.CSS_SELECTOR, '.icon-telegram')
    ICON_YOUTUBE_LOCATOR = (By.CSS_SELECTOR, '.icon-youtube')
    ICON_INSTAGRAM_LOCATOR = (By.CSS_SELECTOR, '.icon-instagram')
    ICON_LINKEDIN_LOCATOR = (By.CSS_SELECTOR, '.icon-linkedin')
    LINK_HILLEL_LOCATOR = (By.CSS_SELECTOR, 'a.contacts_link:nth-child(1)')
    LINK_EMAIL_LOCATOR = (By.CSS_SELECTOR, 'a.contacts_link:nth-child(2)')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def logo_hillel_auto(self):
        return self.element(MainPage.LOGO_HILLEL_AUTO_LOCATOR)

    @property
    def link_email(self):
        return self.element(MainPage.LINK_EMAIL_LOCATOR)

    @property
    def link_hillel(self):
        return self.element(MainPage.LINK_HILLEL_LOCATOR)

    @property
    def icon_linkedin(self):
        return self.element(MainPage.ICON_LINKEDIN_LOCATOR)

    @property
    def icon_instagram(self):
        return self.element(MainPage.ICON_INSTAGRAM_LOCATOR)

    @property
    def icon_youtube(self):
        return self.element(MainPage.ICON_YOUTUBE_LOCATOR)

    @property
    def icon_telegram(self):
        return self.element(MainPage.ICON_TELEGRAM_LOCATOR)

    @property
    def icon_facebook(self):
        return self.element(MainPage.ICON_FACEBOOK_LOCATOR)

    @property
    def text_contacts(self):
        return self.element(MainPage.TEXT_CONTACTS_LOCATOR)

    @property
    def about_section(self):
        return self.element(MainPage.ABOUT_SECTION_LOCATOR)

    @property
    def button_home(self):
        return self.element(MainPage.BUTTON_HOME_LOCATOR)

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

    @allure.step('Open Log in pop-up')
    def open_log_in_pop_up(self):
        self.button_signin.click()
        log_in_pop_up = LoginPopUp(self.driver)
        return log_in_pop_up

    @allure.step('Open Registration pop-up')
    def open_registration_pop_up(self):
        self.button_signup.click()
        registration_pop_up = RegistrationPopUp(self.driver)
        return registration_pop_up

    @allure.step('Click button "Home')
    def click_button_home(self):
        self.button_home.click()

    @allure.step('Click button "About')
    def click_button_about(self):
        self.button_about.click()

    @allure.step('Click button "Contacts')
    def click_button_contacts(self):
        self.button_contacts.click()

    @allure.step('Click icon "Facebook')
    def click_icon_facebook(self):
        self.icon_facebook.click()

    @allure.step('Click icon "Telegram')
    def click_icon_telegram(self):
        self.icon_telegram.click()

    @allure.step('Click icon "Youtube')
    def click_icon_youtube(self):
        self.icon_youtube.click()

    @allure.step('Click icon "Instagram')
    def click_icon_instagram(self):
        self.icon_instagram.click()

    @allure.step('Click icon "LinkedIn')
    def click_icon_linkedin(self):
        self.icon_linkedin.click()

    @allure.step('Click link "ithillel.ua')
    def click_link_hillel(self):
        self.link_hillel.click()

    @allure.step('Click link "support email')
    def click_link_email(self):
        self.link_email.click()









