import allure

@allure.title('Close registration po-up')
def test_registration_pop_up_is_open(driver, main_page):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    assert 'Registration' in registration_pop_up.text_registration.text

@allure.title('Open registration po-up')
def test_registration_pop_close(driver, main_page):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    registration_pop_up.click_close_button()
    driver.implicitly_wait(2)
    main_page.logo_hillel_auto.is_displayed()
    assert registration_pop_up.is_element_not_displayed(registration_pop_up.TEXT_REGISTRATION_LOCATOR)

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


@allure.description('Successful registration')
def test_successful_registration(driver, main_page, test_user2, sidebar):
    with allure.step("Click Sign up button"):
        registration_pop_up = main_page.open_registration_pop_up()
    with allure.step("Fill login form and click registration button"):
        garage_page = registration_pop_up.successful_registration(test_user2.name, test_user2.lastname,
                                                                  test_user2.email, test_user2.password)
    assert garage_page.page_title.is_displayed()
    settings = sidebar.open_settings_page()
    r_a = settings.click_remove_my_account()
    r_a.click_remove_button()





# TODO:
#  - tests for incorrect values;
#  - add additional method for registration user creating;
#
