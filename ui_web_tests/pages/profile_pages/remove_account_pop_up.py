import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from ui_web_tests.pages.base_page import BasePage


class RemoveAccountPopUp(BasePage):

    TEXT_REMOVE_ACCOUNT_LOCATOR = (By.CSS_SELECTOR, '.modal-title')
    BUTTON_REMOVE_LOCATOR = (By.CSS_SELECTOR, '.btn-danger')
    BUTTON_CANCEL_LOCATOR = (By.CSS_SELECTOR, '.modal-footer > button:nth-child(1)')
    BUTTON_CLOSE_LOCATOR = (By.CSS_SELECTOR, '.close > span:nth-child(1)')
    TEXT_QUESTION_LOCATOR = (By.CSS_SELECTOR, '.modal-body > p:nth-child(1)')
    TEXT_DANGER_LOCATOR = (By.CSS_SELECTOR, 'p.text-danger')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def text_remove_account(self):
        return self.element(RemoveAccountPopUp.TEXT_REMOVE_ACCOUNT_LOCATOR)

    @property
    def button_remove(self):
        return self.element(RemoveAccountPopUp.BUTTON_REMOVE_LOCATOR)

    @property
    def button_cancel(self):
        return self.element(RemoveAccountPopUp.BUTTON_CANCEL_LOCATOR)

    @property
    def button_close(self):
        return self.element(RemoveAccountPopUp.BUTTON_CLOSE_LOCATOR)

    @property
    def text_question(self):
        return self.element(RemoveAccountPopUp.TEXT_QUESTION_LOCATOR)

    @property
    def text_danger(self):
        return self.element(RemoveAccountPopUp.TEXT_DANGER_LOCATOR)

    @allure.step('Click "Remove" button')
    def click_remove_button(self):
        #self.button_remove.click()
        webdriver.ActionChains(self.driver).move_to_element(self.button_remove).click(self.button_remove).perform()

    @allure.step('Click "Close" button')
    def click_close_button(self):
        self.button_close.click()

    @allure.step('Click "Cancel" button')
    def click_cancel_button(self):
        self.button_cancel.click()