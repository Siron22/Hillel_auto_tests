import allure


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
def test_successful_login(driver, main_page):
    with allure.step("Click Sign In button"):
        log_in_pop_up = main_page.open_log_in_pop_up()
    with allure.step("Click Sign In button with empty fields"):
        log_in_pop_up.click_login_button()
    assert log_in_pop_up.email_error_marker.is_displayed()
    assert log_in_pop_up.password_error_marker.is_displayed()
    assert log_in_pop_up.email_error_marker.text == "Email required"
    assert log_in_pop_up.password_error_marker.text == "Password required"