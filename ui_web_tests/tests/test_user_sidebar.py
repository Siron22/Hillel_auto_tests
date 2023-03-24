import allure

"""Tests for user profile"""

@allure.title('Sidebar user profile: elements visibility')
def test_sidebar_elements_visibility(authorization, driver, sidebar):
    title = authorization.page_title
    assert 'Garage' in title.text
    assert sidebar.button_garage.is_displayed()
    assert sidebar.button_fuel_expenses.is_displayed()
    assert sidebar.button_instruction.is_displayed()
    assert sidebar.button_profile.is_displayed()
    assert sidebar.button_settings.is_displayed()
    assert sidebar.button_log_out.is_displayed()


@allure.title('Sidebar user profile: Navigate to Fuel expenses')
def test_navigate_to_fuel_expenses(authorization, driver, sidebar):
    f_e_page = sidebar.open_fuel_expenses_page()
    assert 'Fuel expenses' in f_e_page.page_title.text

@allure.title('Sidebar user profile: Navigate to Instructions')
def test_navigate_to_instructions(authorization, driver, sidebar):
    instructions_page = sidebar.open_instructions_page()
    assert 'Instructions' in instructions_page.page_title.text

@allure.title('Sidebar user profile: Navigate to Profile')
def test_navigate_to_profile(authorization, driver, sidebar):
    profile_page = sidebar.open_profile_page()
    assert 'Profile' in profile_page.page_title.text

@allure.title('Sidebar user profile: Navigate to Settings')
def test_navigate_to_profile(authorization, driver, sidebar):
    settings_page = sidebar.open_settings_page()
    assert 'Settings' in settings_page.page_title.text

@allure.title('Sidebar user profile: Navigate to Garage')
def test_navigate_to_profile(authorization, driver, sidebar):
    sidebar.open_settings_page()
    garage_page = sidebar.open_garage_page()
    assert 'Garage' in garage_page.page_title.text

@allure.title('Sidebar user profile: Log out')
def test_log_out_button(authorization, driver, sidebar):
    main_page = sidebar.click_log_out()
    assert main_page.button_home.is_displayed()

