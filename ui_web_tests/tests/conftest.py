import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from ui_web_tests.pages.navigation_elements.sidebar import Sidebar
from ui_web_tests.utilities.browsers import Browser
from settings.useful_func import get_browser_name, get_screenshot_directory
from ui_web_tests.utilities.project_exceptions import UnsupportedBrowserError
from ui_web_tests.pages.main_page_elements.main_page import MainPage
from ui_web_tests.utilities.user import User


@pytest.fixture(scope='session')
def browser_name():
    return get_browser_name()


@pytest.fixture()
def driver(browser_name):
    if browser_name.lower() == Browser.CHROME:
        """Options for headless mode"""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("USER AGENT")
        options.add_argument('--window-size=1920,1080')
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name.lower() == Browser.FIREFOX:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
    else:
        raise UnsupportedBrowserError
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def registered_user():
    return User('Pierce', 'Nicolass', 'Shany.Windler@gmail.com', 'Wednesday1XxXx')

@pytest.fixture(scope='session')
def unregistered_user():
    return User('Andreas', 'Niolass', 'Sha.Windl@gmail.com', 'Wednesday5XxXx')



@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    main_page.navigate_to_main()
    return main_page

@allure.step('Test user authorization')
@pytest.fixture()
def authorization(main_page, registered_user):
    log_in_pop_up = main_page.open_log_in_pop_up()
    garage_page = log_in_pop_up.successful_login(registered_user.email, registered_user.password)
    return garage_page


@pytest.fixture()
def sidebar(driver):
    return Sidebar(driver)


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
        allure.attach.file(file_path, name='Test failed screen', attachment_type=allure.attachment_type.PNG)





