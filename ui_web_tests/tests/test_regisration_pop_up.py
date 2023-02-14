import allure


@allure.title('Open registration po-up')
def test_registration_pop_up_is_open(driver, main_page):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    assert 'Registration' in registration_pop_up.text_registration.text


@allure.description('This test is about all elements visibility')
def test_registration_pop_up_elements_are_visible(driver, main_page):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    assert registration_pop_up.text_registration.is_displayed()
    assert registration_pop_up.button_cross.is_displayed()
    assert registration_pop_up.field_email.is_displayed()
    assert registration_pop_up.field_password.is_displayed()
    assert registration_pop_up.field_reenter_password.is_displayed()
    assert registration_pop_up.field_name.is_displayed()
    assert registration_pop_up.field_last_name.is_displayed()
    assert registration_pop_up.button_register.is_displayed()


@allure.story('Successful registration')
def test_successful_registration(driver, main_page, test_user):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    with allure.step("Fill login form and click registration button"):
        garage_page = registration_pop_up.successful_registration(test_user.name, test_user.lastname,
                                                                  test_user.email, test_user.password)
    assert garage_page.garage_name.is_displayed()

# TODO:
#  - tests for incorrect values;
#  - add additional method for registration user creating;
#  - automate the process of deleting a user.
