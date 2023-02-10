
def test_log_in_pop_up_is_open(log_in_pop_up):
    assert 'Log in' in log_in_pop_up.text_log_in.text


def test_log_in_pop_up_elements_are_visible(log_in_pop_up):
    assert log_in_pop_up.text_log_in.is_displayed()
    assert log_in_pop_up.button_cross.is_displayed()
    assert log_in_pop_up.field_email.is_displayed()
    assert log_in_pop_up.field_password.is_displayed()
    assert log_in_pop_up.check_box_remember_me.is_displayed()
    assert log_in_pop_up.button_forgot_password.is_displayed()
    assert log_in_pop_up.button_registration.is_displayed()
    assert log_in_pop_up.button_login.is_displayed()


def test_remember_me_button_enable(log_in_pop_up):
    log_in_pop_up.remember_me_enable()
    assert log_in_pop_up.check_box_remember_me.is_displayed()
    assert log_in_pop_up.check_box_remember_me.is_selected()


def test_registration_button_click(log_in_pop_up, registration_pop_up):
    log_in_pop_up.click_registration_button()
    assert 'Registration' in registration_pop_up.text_registration.text

    # не получается победить этот метод, пришлось добавить registration_pop_up
    # assert log_in_pop_up.is_element_not_displayed(log_in_pop_up.CHECK_BOX_REMEMBER_ME_LOCATOR)


def test_successful_login(log_in_pop_up, test_user):
    garage_page = log_in_pop_up.successful_login(test_user.email, test_user.password)
    assert garage_page.garage_name.is_displayed()
