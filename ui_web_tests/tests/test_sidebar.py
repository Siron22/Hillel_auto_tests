import allure
from ui_web_tests.pages.navigation_elements.sidebar import Sidebar


@allure.title('Sidebar elements visibility')
def test_sidebar_elements_visibility(authorization, driver):
    title = authorization.page_title
    sidebar = Sidebar(driver)
    assert 'Garage' in title.text
    assert sidebar.button_garage.is_displayed()
    assert sidebar.button_fuel_expenses.is_displayed()
    assert sidebar.button_instruction.is_displayed()
    assert sidebar.button_profile.is_displayed()
    assert sidebar.button_settings.is_displayed()
    assert sidebar.button_log_out.is_displayed()


@allure.title('Sidebar: Navigate to Fuel expenses')
def test_navigate_to_fuel_expenses(authorization, driver):
    sidebar = Sidebar(driver)
    f_e_page = sidebar.open_fuel_expenses_page()
    assert 'Fuel expenses' in f_e_page.page_title.text

@allure.title('Sidebar: Navigate to Instructions')
def test_navigate_to_instructions(authorization, driver):
    sidebar = Sidebar(driver)
    instructions_page = sidebar.open_instructions_page()
    assert 'Instructions' in instructions_page.page_title.text

@allure.title('Sidebar: Navigate to Profile')
def test_navigate_to_profile(authorization, driver):
    sidebar = Sidebar(driver)
    profile_page = sidebar.open_profile_page()
    assert 'Profile' in profile_page.page_title.text

@allure.title('Sidebar: Navigate to Settings')
def test_navigate_to_profile(authorization, driver):
    sidebar = Sidebar(driver)
    settings_page = sidebar.open_settings_page()
    assert 'Settings' in settings_page.page_title.text

@allure.title('Sidebar: Navigate to Garage')
def test_navigate_to_profile(authorization, driver):
    sidebar = Sidebar(driver)
    sidebar.open_settings_page()
    garage_page = sidebar.open_garage_page()
    assert 'Garage' in garage_page.page_title.text

@allure.title('Sidebar: Log out')
def test_log_out_button(authorization, driver):
    sidebar = Sidebar(driver)
    main_page = sidebar.click_log_out()
    assert main_page.button_home.is_displayed()

