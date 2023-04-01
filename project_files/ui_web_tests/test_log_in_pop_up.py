import time
import allure
import pytest
from pytest_check import check
from project_files.utilities.alerts import Alerts
from project_files.instances.user import UserTestData


@allure.title('Login pop-up open')
def test_log_in_pop_up_is_open(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    assert 'Log in' in log_in_pop_up.text_log_in.text


@allure.title('Login pop-up close')
def test_log_in_pop_up_close(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    log_in_pop_up.click_close_button()
    time.sleep(1)
    assert log_in_pop_up.element_is_not_visible(log_in_pop_up.BUTTON_LOGIN_LOCATOR)


@allure.title('Visibility of pop-up elements')
def test_log_in_pop_up_elements_are_visible(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    driver.implicitly_wait(2)
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.TEXT_LOG_IN_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.BUTTON_CLOSE_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.FIELD_EMAIL_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.FIELD_PASSWORD_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.CHECK_BOX_REMEMBER_ME_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.BUTTON_FORGOT_PASSWORD_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.BUTTON_REGISTRATION_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.BUTTON_LOGIN_LOCATOR))


@allure.feature('Remember me')
def test_remember_me_button_enable(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    log_in_pop_up.remember_me_enable()
    assert log_in_pop_up.check_box_remember_me.is_selected()


@allure.description('Registration pop-up open')
def test_registration_button_click(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    registration_pop_up = log_in_pop_up.click_registration_button()
    check.is_true(log_in_pop_up.element_is_not_visible(log_in_pop_up.CHECK_BOX_REMEMBER_ME_LOCATOR))
    time.sleep(1)
    assert 'Registration' in registration_pop_up.text_registration.text


@allure.description('Restore access pop-up open')
def test_forgot_password_button_click(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    restore_access_pop_up = log_in_pop_up.click_forgot_password_button()
    check.is_true(log_in_pop_up.element_is_not_visible(log_in_pop_up.CHECK_BOX_REMEMBER_ME_LOCATOR))
    assert 'Restore access' in restore_access_pop_up.text_restore.text


@allure.feature('Login')
@allure.description('Successful login')
def test_successful_login(driver, main_page, registered_user):
    log_in_pop_up = main_page.open_log_in_pop_up()
    garage_page = log_in_pop_up.successful_login(registered_user.email, registered_user.password)
    assert garage_page.page_title.is_displayed()

"""Negative tests"""

@allure.feature('Login')
@allure.description('Test for all empty fields')
def test_unsuccessful_login_empty_fields(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Click email field"):
        log_in_pop_up.field_email.click()
    with allure.step("Click password field"):
        log_in_pop_up.field_password.click()
    with allure.step("Click remember me button"):
        log_in_pop_up.remember_me_enable()
    check.is_false(log_in_pop_up.button_login.is_enabled())
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    if log_in_pop_up.element_is_visible(log_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.EMAIL_REQUIRED, log_in_pop_up.email_error_marker.text)
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    if log_in_pop_up.element_is_visible(log_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR):
        check.equal(Alerts.PASSWORD_REQUIRED, log_in_pop_up.password_error_marker.text)


@allure.feature('Login')
@allure.description('Test for incorrect email')
@pytest.mark.parametrize('email', UserTestData.INVALID_EMAIL_DATA)
def test_unsuccessful_login_incorrect_email(driver, main_page, email):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter incorrect data in email field"):
        log_in_pop_up.enter_email(email)
    with allure.step("Enter random value in password field"):
        log_in_pop_up.enter_password(UserTestData.VALID_PASSWORD)
    check.is_false(log_in_pop_up.button_login.is_enabled())
    check.is_true(log_in_pop_up.element_is_not_visible(log_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR))
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR))
    if log_in_pop_up.element_is_visible(log_in_pop_up.EMAIL_ERROR_MARKER_LOCATOR):
        check.equal(log_in_pop_up.email_error_marker.text, Alerts.EMAIL_IS_INCORRECT)


@allure.feature('Login')
@allure.description('Test for incorrect password')
def test_unsuccessful_login_incorrect_password(driver, main_page, registered_user):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter correct data in email field"):
        log_in_pop_up.enter_email(registered_user.email)
    with allure.step("Enter incorrect value in password field"):
        log_in_pop_up.enter_password(UserTestData.VALID_PASSWORD)
    check.is_true(log_in_pop_up.button_login.is_enabled())
    log_in_pop_up.click_login_button()
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR))
    if log_in_pop_up.element_is_visible(log_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR):
        check.equal(log_in_pop_up.alert_wrong_email_or_password.text, Alerts.WRONG_EMAIL_OR_PASSWORD)


@allure.feature('Login')
@allure.description('Test for unregistered user')
def test_unsuccessful_login_unregistered_user(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter  in email field unregistered email"):
        log_in_pop_up.enter_email(UserTestData.UNREGISTERED_EMAIL)
    with allure.step("Enter incorrect value in password field"):
        log_in_pop_up.enter_password(UserTestData.VALID_PASSWORD)
    check.is_true(log_in_pop_up.button_login.is_enabled())
    log_in_pop_up.click_login_button()
    check.is_true(log_in_pop_up.element_is_visible(log_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR))
    if log_in_pop_up.element_is_visible(log_in_pop_up.ALERT_WRONG_EMAIL_OR_PASSWORD_LOCATOR):
        check.equal(log_in_pop_up.alert_wrong_email_or_password.text, Alerts.WRONG_EMAIL_OR_PASSWORD)



