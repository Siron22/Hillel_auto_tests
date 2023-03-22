import allure
import pytest
from pytest_check import check

from ui_web_tests.utilities.alerts import Alerts
from ui_web_tests.utilities.user import UserDataIncorrect


@allure.title('Close registration po-up')
def test_registration_pop_up_is_open(driver, main_page):
    registration_pop_up = main_page.open_registration_pop_up()
    assert 'Registration' in registration_pop_up.text_registration.text


@allure.title('Open registration po-up')
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
    registration_in_pop_up = main_page.open_registration_pop_up()
    with allure.step("Click Name field"):
        registration_in_pop_up.field_name.click()
    with allure.step("Click Last name field"):
        registration_in_pop_up.field_last_name.click()
    with allure.step("Click email field"):
        registration_in_pop_up.field_email.click()
    with allure.step("Click password field"):
        registration_in_pop_up.field_password.click()
    with allure.step("Click re-enter password field"):
        registration_in_pop_up.field_reenter_password.click()
    registration_in_pop_up.field_password.click()
    check.is_false(registration_in_pop_up.button_register.is_enabled())
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.NAME_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.NAME_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.NAME_REQUIRED, registration_in_pop_up.name_error_marker.text)
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.LAST_NAME_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.LAST_NAME_REQUIRED, registration_in_pop_up.last_name_error_marker.text)
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.EMAIL_REQUIRED, registration_in_pop_up.email_error_marker.text)
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.PASSWORD_REQUIRED, registration_in_pop_up.password_error_marker.text)
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.RE_ENTER_PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.RE_ENTER_PASSWORD_REQUIRED, registration_in_pop_up.re_enter_password_error_marker.text)

"""********************************"""

@allure.feature('Registration')
@allure.description('Test for incorrect name value: russian symbols, numbers, special symbols, name with space')
@pytest.mark.parametrize('name', UserDataIncorrect.INCORRECT_NAME_DATA)
def test_unsuccessful_registration_incorrect_name(driver, main_page, name):
    registration_in_pop_up = main_page.open_registration_in_pop_up()
    with allure.step("Enter incorrect data in name field"):
        registration_in_pop_up.enter_name(name)
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.NAME_ERROR_MARKER_LOCATOR))
    if registration_in_pop_up.element_is_visible(registration_in_pop_up.NAME_ERROR_MARKER_LOCATOR):
        check.equal(registration_in_pop_up.email_error_marker.text, Alerts.EMAIL_IS_INCORRECT)


@allure.feature('Registration')
@allure.description('Test for incorrect email')
@pytest.mark.parametrize('email, password', UserDataIncorrect.INVALID_EMAIL_DATA)
def test_unsuccessful_login_incorrect_email(driver, main_page, email, password):
    registration_in_pop_up = main_page.open_registration_in_pop_up()
    with allure.step("Enter incorrect data in email field"):
        registration_in_pop_up.enter_email(email)
    with allure.step("Enter random value in password field"):
        registration_in_pop_up.enter_password(UserDataIncorrect.RANDOM_PASSWORD)
    check.is_false(registration_in_pop_up.button_login.is_enabled())
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    check.is_true(registration_in_pop_up.element_is_not_visible(registration_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    check.equal(registration_in_pop_up.email_error_marker.text, Alerts.EMAIL_IS_INCORRECT)


@allure.feature('Registration')
@allure.description('Test for incorrect email')
@pytest.mark.parametrize('email, password', UserDataIncorrect.INVALID_EMAIL_DATA)
def test_unsuccessful_login_incorrect_email(driver, main_page, email, password):
    registration_in_pop_up = main_page.open_registration_in_pop_up()
    with allure.step("Enter incorrect data in email field"):
        registration_in_pop_up.enter_email(email)
    with allure.step("Enter random value in password field"):
        registration_in_pop_up.enter_password(UserDataIncorrect.RANDOM_PASSWORD)
    check.is_false(registration_in_pop_up.button_login.is_enabled())
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    check.is_true(registration_in_pop_up.element_is_not_visible(registration_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    check.equal(registration_in_pop_up.email_error_marker.text, Alerts.EMAIL_IS_INCORRECT)


@allure.feature('Registration')
@allure.description('Test for incorrect password')
def test_unsuccessful_login_incorrect_password(driver, main_page, registered_user):
    registration_in_pop_up = main_page.open_registration_in_pop_up()
    with allure.step("Enter correct data in email field"):
        registration_in_pop_up.enter_email(registered_user.email)
    with allure.step("Enter incorrect value in password field"):
        registration_in_pop_up.enter_password(UserDataIncorrect.RANDOM_PASSWORD)
    check.is_true(registration_in_pop_up.button_login.is_enabled())
    registration_in_pop_up.click_login_button()
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR))
    check.equal(registration_in_pop_up.alert_wrong_email_or_password.text, Alerts.WRONG_EMAIL_OR_PASSWORD)


@allure.feature('Registration')
@allure.description('Test for unregistered user')
def test_unsuccessful_login_unregistered_user(driver, main_page):
    registration_in_pop_up = main_page.open_registration_in_pop_up()
    with allure.step("Enter  in email field unregistered email"):
        registration_in_pop_up.enter_email(UserDataIncorrect.UNREGISTERED_EMAIL)
    with allure.step("Enter incorrect value in password field"):
        registration_in_pop_up.enter_password(UserDataIncorrect.RANDOM_PASSWORD)
    check.is_true(registration_in_pop_up.button_login.is_enabled())
    registration_in_pop_up.click_login_button()
    check.is_true(registration_in_pop_up.element_is_visible(registration_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR))
    check.equal(registration_in_pop_up.alert_wrong_email_or_password.text, Alerts.WRONG_EMAIL_OR_PASSWORD)




