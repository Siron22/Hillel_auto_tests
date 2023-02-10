def test_registration_pop_up_is_open(registration_pop_up):
    assert 'Registration' in registration_pop_up.text_registration.text


def test_registration_pop_up_elements_are_visible(registration_pop_up):
    assert registration_pop_up.text_registration.is_displayed()
    assert registration_pop_up.button_cross.is_displayed()
    assert registration_pop_up.field_email.is_displayed()
    assert registration_pop_up.field_password.is_displayed()
    assert registration_pop_up.field_reenter_password.is_displayed()
    assert registration_pop_up.field_name.is_displayed()
    assert registration_pop_up.field_last_name.is_displayed()
    assert registration_pop_up.button_register.is_displayed()


def test_successful_registration(registration_pop_up, test_user):
    garage_page = registration_pop_up.successful_registration(test_user.name, test_user.lastname, test_user.email,
                                                              test_user.password)
    assert garage_page.garage_name.is_displayed()

# TODO:
#  - tests for incorrect values;
#  - add additional method for registration user creating;
#  - automate the process of deleting a user.

