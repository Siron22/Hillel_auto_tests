import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from ui_web_tests.utilities.browsers import Browser
from ui_web_tests.utilities.useful_func import get_browser_name, get_screenshot_directory
from ui_web_tests.utilities.project_exceptions import UnsupportedBrowserError
from ui_web_tests.pages.main_page import MainPage
from ui_web_tests.utilities.user import User
from ui_web_tests.pages.log_in_pop_up import LoginPopUp
from ui_web_tests.pages.registration_pop_up import RegistrationPopUp
from ui_web_tests.pages.restore_access_page import RestoreAccessPage


@pytest.fixture(scope='session')
def browser_name():
    return get_browser_name()


@pytest.fixture()
def driver(browser_name):
    if browser_name.lower() == Browser.CHROME:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
    elif browser_name.lower() == Browser.FIREFOX:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
    else:
        raise UnsupportedBrowserError
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def test_user():
    return User("Pierce", "Nicolas", "Shany.Windler@gmail.com", "Wednesday1XxXx")


@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    main_page.navigate()
    return main_page


@pytest.fixture()
def log_in_pop_up(driver):
    main_page = MainPage(driver)
    main_page.navigate()
    main_page.click_sign_in_button()
    log_in_pop_up = LoginPopUp(driver)
    return log_in_pop_up


@pytest.fixture()
def registration_pop_up(driver):
    main_page = MainPage(driver)
    main_page.navigate()
    main_page.click_sign_up_button()
    registration_pop_up = RegistrationPopUp(driver)
    return registration_pop_up


@pytest.fixture()
def class_registration_pop_up(driver):
    class_registration_pop_up = RegistrationPopUp(driver)
    return class_registration_pop_up


@pytest.fixture()
def class_restore_access_pop_up(driver):
    class_restore_access_pop_up = RestoreAccessPage(driver)
    return class_restore_access_pop_up


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:

        driver = item.funcargs["driver"]
        import datetime
        file_name = f"{item.name}_{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.png"
        file_path = os.path.join(get_screenshot_directory(), file_name)
        driver.save_screenshot(file_path)
        # allure.attach(driver.get_, name='My Test', attachment_type=allure.attachment_type.TEXT)

# TODO разобраться почему не запускается Опера