import allure
import pytest_check
from pytest_check import check
from ui_web_tests.pages.main_page_elements.main_page import MainPage


@allure.title('Main test for main page')
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_is_open(driver, main_page):
    with allure.step("Verify title"):
        assert 'Hillel Qauto' in driver.title


@allure.description('Test for all main paige elements visibility')
def test_main_page_elements_displayed(driver, main_page):
    assert main_page.video_locator.is_displayed()
    assert main_page.logo_hillel_auto.is_displayed()
    assert main_page.button_home.is_displayed()
    assert main_page.button_about.is_displayed()
    assert main_page.button_contacts.is_displayed()
    assert main_page.button_guest_login.is_displayed()
    assert main_page.button_signin.is_displayed()
    assert main_page.button_signup.is_displayed()
    assert main_page.string1.is_displayed()
    assert main_page.string2.is_displayed()


# @allure.description('Test for all main paige elements visibility')
# def test_main_page_elements_displayed(driver):
#     main_page = MainPage(driver)
#     main_page.navigate_to_main()
#     pytest_check.check.is_true(main_page.video_locator.is_displayed())
#     with pytest_check.check:
#         assert main_page.logo_hillel_auto.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_home.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_about.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_contacts.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_guest_login.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_signin.is_displayed()
#     with pytest_check.check:
#         assert main_page.button_signup.is_displayed()
#     with pytest_check.check:
#         assert main_page.string1.is_displayed()
#     with pytest_check.check:
#         assert main_page.string2.is_displayed()
#      pytest_check.check.is_true(main_page.video_locator.is_displayed())

@allure.issue('http://jira.com', name='BUG-X3')
def test_main_page_video_displayed(driver, main_page):
    """Визуально объект присутствует, а тест почему-то падает"""
    assert main_page.video_locator.is_displayed()

"""
Not tests!!!
Only features verify
"""

@allure.title('Scroll the page')
def test_main_page_scroll_to_end(driver, main_page):
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    import time
    time.sleep(2)

@allure.title('Click button "Home"')
def test_main_page_click_home(driver, main_page):
    main_page.click_button_home

@allure.title('Click button "About"')
def test_main_page_click_about(driver, main_page):
    main_page.click_button_about

@allure.title('Click button "Contacts"')
def test_main_page_click_contacts(driver, main_page):
    main_page.click_button_contacts

# TODO: Make launch video test

# def test_pytest_check():
#     with pytest_check.check:
#         assert 2 == 3
#     check.equal(2, 3)
#     assert True