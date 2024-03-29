from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from project_files.pages.base_page import BasePage

class ProfilePage(BasePage):

    INSTRUCTIONS_LOCATOR = (By.CSS_SELECTOR, '.panel-page_heading > h1')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def page_title(self):
        return self.element(ProfilePage.INSTRUCTIONS_LOCATOR)