import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from hillel_auto.utilities.browsers import Browser
from hillel_auto.utilities.useful_func import get_browser_name, get_screenshot_directory, get_base_url
from hillel_auto.utilities.project_exceptions import UnsupportedBrowserError
from hillel_auto.pages.main_page import MainPage
from hillel_auto.utilities.user import User


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
    elif browser_name.lower() == Browser.OPERA:
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        driver.maximize_window()
    else:
        raise UnsupportedBrowserError
    yield driver
    driver.quit()

@pytest.fixture()
def main_page(driver):
    main_page = MainPage(driver)
    main_page.navigate()
    return main_page


@pytest.fixture(scope='session')
def valid_user():
    return User("Pierce", "Nicolas", "Shany.Windler@gmail.com", "Wednesday1XxXx")


# @pytest.fixture(scope='session')
# def locked_out_user():
#     return User('locked_out_user', 'secret_sauce')
#
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):  # pylint: disable=unused-argument
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#
#         driver = item.funcargs["driver"]
#         import datetime
#         file_name = f"{item.name}_{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M')}.png"
#         file_path = os.path.join(get_screenshot_directory(), file_name)
#         driver.save_screenshot(file_path)
#         #allure.attach(driver.get_, name='My Test', attachment_type=allure.attachment_type.TEXT)