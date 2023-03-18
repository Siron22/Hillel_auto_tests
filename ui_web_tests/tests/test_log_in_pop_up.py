import allure
import pytest
from pytest_check import check
from ui_web_tests.utilities.user import User


@allure.title('Login pop-up open')
def test_log_in_pop_up_is_open(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    assert 'Log in' in log_in_pop_up.text_log_in.text

@allure.title('Login pop-up close')
def test_log_in_pop_up_close(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    log_in_pop_up.click_close_button()
    driver.implicitly_wait(2)
    main_page.logo_hillel_auto.is_displayed()
    assert log_in_pop_up.is_element_not_displayed(log_in_pop_up.TEXT_LOG_IN_LOCATOR)

@allure.title('Visibility of pop-up elements')
def test_log_in_pop_up_elements_are_visible(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    assert log_in_pop_up.text_log_in.is_displayed()
    assert log_in_pop_up.button_cross.is_displayed()
    assert log_in_pop_up.field_email.is_displayed()
    assert log_in_pop_up.field_password.is_displayed()
    assert log_in_pop_up.check_box_remember_me.is_displayed()
    assert log_in_pop_up.button_forgot_password.is_displayed()
    assert log_in_pop_up.button_registration.is_displayed()
    assert log_in_pop_up.button_login.is_displayed()


@allure.feature('Remember me')
def test_remember_me_button_enable(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enable remember me button"):
        log_in_pop_up.remember_me_enable()
    assert log_in_pop_up.check_box_remember_me.is_displayed()
    assert log_in_pop_up.check_box_remember_me.is_selected()


@allure.description('This test is for open registration pop-up')
def test_registration_button_click(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Click registration button"):
        registration_pop_up = log_in_pop_up.click_registration_button()
    assert 'Registration' in registration_pop_up.text_registration.text
    assert log_in_pop_up.is_element_not_displayed(log_in_pop_up.CHECK_BOX_REMEMBER_ME_LOCATOR)


@allure.feature('Restore password')
@allure.description('This test is for open restore access pop-up')
def test_forgot_password_button_click(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Click button Forgot password"):
        restore_access_pop_up = log_in_pop_up.click_forgot_password_button()
    assert 'Restore access' in restore_access_pop_up.text_restore.text


@allure.feature('Login')
@allure.description('Successful login')
def test_successful_login(driver, main_page, test_user):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Fill login form and click Sign In button"):
        garage_page = log_in_pop_up.successful_login(test_user.email, test_user.password)
    assert garage_page.page_title.is_displayed()

"""Negative tests"""

@allure.feature('Login')
@allure.description('Test for all empty fields')
def test_unsuccessful_login_empty_fields(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Click email field"):
        log_in_pop_up.field_email.click()
    with allure.step("Click password field"):
        log_in_pop_up.field_password.click()
    with allure.step("Click remember me button"):
        log_in_pop_up.remember_me_enable()
    assert log_in_pop_up.button_login.is_enabled() == False
    assert log_in_pop_up.email_error_marker.is_displayed()
    assert log_in_pop_up.password_error_marker.is_displayed()
    check.equal(log_in_pop_up.email_error_marker.text, "Email required")
    check.equal(log_in_pop_up.password_error_marker.text, "Password required")


@allure.feature('Login')
@allure.description('Test for incorrect email')
@pytest.mark.parametrize('email, password', User.INVALID_EMAIL_DATA)
def test_unsuccessful_login_incorrect_email(driver, main_page, email, password):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter incorrect data in email field"):
        log_in_pop_up.enter_email(email)
    with allure.step("Enter random value in password field"):
        log_in_pop_up.enter_password(password)
    check.equal(log_in_pop_up.button_login.is_enabled(), False)
    assert log_in_pop_up.email_error_marker.text == "Email is incorrect"
    assert log_in_pop_up.email_error_marker.is_displayed()
    assert log_in_pop_up.is_element_not_displayed(log_in_pop_up.PASSWORD_ERROR_MARKER_LOCATOR)


@allure.feature('Login')
@allure.description('Test for incorrect password')
def test_unsuccessful_login_incorrect_password(driver, main_page, test_user):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter correct data in email field"):
        log_in_pop_up.enter_email(test_user.email)
    with allure.step("Enter incorrect value in password field"):
        log_in_pop_up.enter_password(User.INCORRECT_PASSWORD)
    check.equal(log_in_pop_up.button_login.is_enabled(), True)
    log_in_pop_up.click_login_button()
    assert log_in_pop_up.alert_wrong_email_or_password.is_displayed()
    assert log_in_pop_up.alert_wrong_email_or_password.text == 'Wrong email or password'

@allure.feature('Login')
@allure.description('Test for unregistered user')
def test_unsuccessful_login_unregistered_user(driver, main_page):
    log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Enter  in email field unregistered email"):
        log_in_pop_up.enter_email(User.UNREGISTERED_EMAIL)
    with allure.step("Enter incorrect value in password field"):
        log_in_pop_up.enter_password(User.INCORRECT_PASSWORD)
    check.equal(log_in_pop_up.button_login.is_enabled(), True)
    log_in_pop_up.click_login_button()
    assert log_in_pop_up.alert_wrong_email_or_password.is_displayed()
    assert log_in_pop_up.alert_wrong_email_or_password.text == 'Wrong email or password'

