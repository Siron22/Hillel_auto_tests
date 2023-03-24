import time
import allure
import pytest
from pytest_check import check
from selenium.webdriver.common.by import By

from ui_web_tests.utilities.alerts import Alerts
from ui_web_tests.utilities.user import UserTestData


@allure.title('Close registration pop-up')
def test_registration_pop_up_is_open(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    assert 'Registration' in registration_pop_up.text_registration.text


@allure.title('Open registration pop-up')
def test_registration_pop_close(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    registration_pop_up.click_close_button()
    main_page.logo_hillel_auto.is_displayed()
    assert registration_pop_up.element_is_not_visible(registration_pop_up.TEXT_REGISTRATION_LOCATOR)


@allure.description('This test is about all elements visibility')
def test_registration_pop_up_elements_are_visible(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.TEXT_REGISTRATION_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.BUTTON_CLOSE_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.FIELD_EMAIL_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.FIELD_PASSWORD_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.FIELD_REENTER_PASSWORD_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.FIELD_NAME_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.FIELD_LAST_NAME_LOCATOR))
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.BUTTON_REGISTER_LOCATOR))


@allure.feature('Registration')
@allure.description('Successful registration')
def test_successful_registration(driver, main_page, unregistered_user, sidebar):
    registration_pop_up = main_page.open_registration_pop_up()
    garage_page = registration_pop_up.successful_registration(unregistered_user.name, unregistered_user.lastname,
                                                              unregistered_user.email, unregistered_user.password)
    assert garage_page.element_is_visible(garage_page.PAGE_TITLE_LOCATOR)
    """Tear down after test"""
    settings = sidebar.open_settings_page()
    remove_account = settings.click_remove_my_account()
    remove_account.click_remove_button()

"""Negative tests"""

@allure.feature('Registration')
@allure.description('Test for all empty fields in registration pop-up')
def test_unsuccessful_login_empty_fields(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Click "Name" field'):
        registration_pop_up.field_name.click()
    with allure.step('Click "Last name" field'):
        registration_pop_up.field_last_name.click()
    with allure.step('Click "Email" field'):
        registration_pop_up.field_email.click()
    with allure.step('Click "Password" field'):
        registration_pop_up.field_password.click()
    with allure.step('Click "Re-enter" password field'):
        registration_pop_up.field_reenter_password.click()
    registration_pop_up.field_password.click()
    check.is_false(registration_pop_up.button_register.is_enabled())
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.NAME_REQUIRED, registration_pop_up.name_error_marker.text)
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.LAST_NAME_REQUIRED, registration_pop_up.last_name_error_marker.text)
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.EMAIL_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.EMAIL_REQUIRED, registration_pop_up.email_error_marker.text)
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.PASSWORD_REQUIRED, registration_pop_up.password_error_marker.text)
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.RE_ENTER_PASSWORD_REQUIRED, registration_pop_up.re_enter_password_error_marker.text)


@allure.feature('Registration')
@allure.description('Test for incorrect name value and length: 1 invalid symbol, 21 symbol including invalids, '
                    'сyrillic symbols, numbers, special symbols, name with space')
@pytest.mark.parametrize('name', UserTestData.INCORRECT_NAME_DATA)
def test_unsuccessful_registration_incorrect_value_name(driver, main_page, name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Name" field'):
        registration_pop_up.enter_name(name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    length = len(name)
    if 2 <= length <= 20 :
        check.is_true(registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR))
        if registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR):
            check.equal(registration_pop_up.name_error_marker.text, Alerts.NAME_IS_INVALID)
        check.is_in('is-invalid', registration_pop_up.field_name.get_attribute("class"))
    else:
        markers = driver.find_elements(By.XPATH, "//input[@id='signupName']/following-sibling::div/p")
        alerts = []
        for m in markers:
            alerts.append(m.text)
        check.is_in(Alerts.NAME_IS_INVALID, alerts)
        check.is_in(Alerts.NAME_HAS_TO, alerts)
        check.is_in('is-invalid', registration_pop_up.field_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for incorrect length of name')
@pytest.mark.parametrize('name', UserTestData.INCORRECT_LENGTH_DATA)
def test_unsuccessful_registration_incorrect_length_name(driver, main_page, name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Name" field'):
        registration_pop_up.enter_name(name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.name_error_marker.text, Alerts.NAME_HAS_TO)
    check.is_in('is-invalid', registration_pop_up.field_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for trim function in "Name" field')
@pytest.mark.parametrize('name', UserTestData.TRIM_DATA)
def test_unsuccessful_registration_incorrect_trim_in_name(driver, main_page, name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter correct data with space in "Name" field'):
        registration_pop_up.enter_name(name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    check.is_false(registration_pop_up.element_is_visible(registration_pop_up.NAME_ERROR_MARKER_LOCATOR))
    check.is_in('ng-valid', registration_pop_up.field_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for incorrect last name value and length: 1 invalid symbol, 21 symbol including invalids, '
                    'сyrillic symbols, numbers, special symbols, name with space')
@pytest.mark.parametrize('last_name', UserTestData.INCORRECT_NAME_DATA)
def test_unsuccessful_registration_incorrect_value_last_name(driver, main_page, last_name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Last name" field'):
        registration_pop_up.enter_last_name(last_name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    length = len(last_name)
    if 2 <= length <= 20 :
        check.is_true(registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR))
        if registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR):
            check.equal(registration_pop_up.last_name_error_marker.text, Alerts.LAST_NAME_IS_INVALID)
        check.is_in('is-invalid', registration_pop_up.field_last_name.get_attribute("class"))
    else:
        """Tests for both error markers"""
        markers = driver.find_elements(By.XPATH, "//input[@id='signupLastName']/following-sibling::div/p")
        alerts = []
        for m in markers:
            alerts.append(m.text)
        check.is_in(Alerts.LAST_NAME_IS_INVALID, alerts)
        check.is_in(Alerts.LAST_NAME_HAS_TO, alerts)
        check.is_in('is-invalid', registration_pop_up.field_last_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for incorrect length of last name')
@pytest.mark.parametrize('last_name', UserTestData.INCORRECT_LENGTH_DATA)
def test_unsuccessful_registration_incorrect_length_last_name(driver, main_page, last_name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Last name" field'):
        registration_pop_up.enter_last_name(last_name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.last_name_error_marker.text, Alerts.LAST_NAME_HAS_TO)
    check.is_in('is-invalid', registration_pop_up.field_last_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for trim function in "Last name" field')
@pytest.mark.parametrize('last_name', UserTestData.TRIM_DATA)
def test_unsuccessful_registration_trim_in_last_name(driver, main_page, last_name):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter correct data with space in "Last name" field'):
        registration_pop_up.enter_last_name(last_name)
    with allure.step('Click on other field'):
        registration_pop_up.field_password.click()
    check.is_false(registration_pop_up.element_is_visible(registration_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR))
    check.is_in('ng-valid', registration_pop_up.field_last_name.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for incorrect email value')
@pytest.mark.parametrize('email', UserTestData.INVALID_EMAIL_DATA)
def test_unsuccessful_registration_incorrect_email(driver, main_page, email):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Email" field'):
        registration_pop_up.enter_email(email)
    with allure.step("Click on other field"):
        registration_pop_up.field_password.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.EMAIL_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.email_error_marker.text, Alerts.EMAIL_IS_INCORRECT)
    check.is_in('is-invalid', registration_pop_up.field_email.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Tests for incorrect password values in "Password" field: 7 symbol, 16 symbols, only numbers, '
                    'only letters, only capital letters, only small letters, numbers with capital letters, '
                    'numbers with small letters, сyrillic symbols')
@pytest.mark.parametrize('password', UserTestData.INCORRECT_PASSWORD_DATA)
def test_unsuccessful_registration_incorrect_re_enter_password(driver, main_page, password):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Password" field'):
        registration_pop_up.enter_password(password)
    with allure.step("Click on other field"):
        registration_pop_up.field_email.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.password_error_marker.text, Alerts.PASS_HAVE_TO)
    check.is_in('is-invalid', registration_pop_up.field_password.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Tests for incorrect password values in "Re-enter Password" field: 7 symbol, 16 symbols, '
                    'only numbers, only letters, only capital letters, only small letters, numbers with capital letters, '
                    'numbers with small letters, сyrillic symbols')
@pytest.mark.parametrize('password', UserTestData.INCORRECT_PASSWORD_DATA)
def test_unsuccessful_registration_incorrect_password(driver, main_page, password):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Re-enter password" field'):
        registration_pop_up.reenter_password(password)
    with allure.step("Click on other field"):
        registration_pop_up.field_email.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.re_enter_password_error_marker.text, Alerts.PASS_HAVE_TO)
    check.is_in('is-invalid', registration_pop_up.field_reenter_password.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Tests for field "Re-enter password" with other value then in "Password" field')
def test_unsuccessful_registration_re_enter_password_not_match(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter incorrect data in "Password" field'):
        registration_pop_up.enter_password(UserTestData.VALID_PASSWORD)
    with allure.step('Enter any other data in "Re-enter password" field'):
        registration_pop_up.reenter_password(UserTestData.OTHER_PASSWORD)
    with allure.step("Click on other field"):
        registration_pop_up.field_email.click()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.re_enter_password_error_marker.text, Alerts.PASS_NOT_MATCH)
    check.is_in('is-invalid', registration_pop_up.field_reenter_password.get_attribute("class"))


@allure.feature('Registration')
@allure.description('Test for unregistered user')
def test_unsuccessful_registration_registered_user(driver, main_page, registered_user, unregistered_user):
    registration_pop_up = main_page.open_registration_pop_up()
    with allure.step('Enter valid name in "Name" field'):
        registration_pop_up.enter_name(unregistered_user.name)
    with allure.step('Enter valid last name in "Last name" field'):
        registration_pop_up.enter_last_name(unregistered_user.lastname)
    with allure.step('Enter email of registered user in "Email" field'):
        registration_pop_up.enter_email(registered_user.email)
    with allure.step('Enter valid password in "Password" field'):
        registration_pop_up.enter_password(unregistered_user.password)
    with allure.step('Re-enter valid password in "Re-enter" password field'):
        registration_pop_up.reenter_password(unregistered_user.password)
    with allure.step('Click "Registration" button'):
        registration_pop_up.click_registration_button()
    check.is_true(registration_pop_up.element_is_visible(registration_pop_up.USER_EXIST_ERROR_MARKER_LOCATOR))
    if registration_pop_up.element_is_visible(registration_pop_up.USER_EXIST_ERROR_MARKER_LOCATOR):
        check.equal(registration_pop_up.user_exist_error_marker.text, Alerts.USER_ALREADY_EXISTS)







