import allure
from ui_web_tests.pages.navigation_elements.sidebar import Sidebar

"""Tests for guest profile"""

@allure.title('Sidebar guest profile: elements visibility')
def test_sidebar_elements_visibility(main_page, sidebar):
    main_page.click_button_guest_login()
    assert sidebar.button_garage.is_displayed()
    assert sidebar.button_fuel_expenses.is_displayed()
    assert sidebar.button_instruction.is_displayed()
    assert sidebar.button_log_out_guest.is_displayed()

@allure.title('Sidebar guest profile: elements for user profile are absent')
def test_sidebar_elements_visibility(main_page, sidebar):
    main_page.click_button_guest_login()
    assert sidebar.element_is_not_visible(sidebar.BUTTON_PROFILE_LOCATOR)
    assert sidebar.element_is_not_visible(sidebar.BUTTON_SETTINGS_LOCATOR)

@allure.title('Sidebar guest profile: Navigate to Fuel expenses')
def test_navigate_to_fuel_expenses(main_page, sidebar):
    main_page.click_button_guest_login()
    f_e_page = sidebar.open_fuel_expenses_page()
    assert 'Fuel expenses' in f_e_page.page_title.text

@allure.title('Sidebar guest profile: Navigate to Instructions')
def test_navigate_to_instructions(main_page, sidebar):
    main_page.click_button_guest_login()
    instructions_page = sidebar.open_instructions_page()
    assert 'Instructions' in instructions_page.page_title.text

@allure.title('Sidebar guest profile: Navigate to Garage')
def test_navigate_to_profile(main_page, sidebar):
    main_page.click_button_guest_login()
    sidebar.open_instructions_page()
    garage_page = sidebar.open_garage_page()
    assert 'Garage' in garage_page.page_title.text

@allure.title('Sidebar guest profile: Log out')
def test_log_out_button(main_page, driver, sidebar):
    main_page.click_button_guest_login()
    sidebar.click_log_out_guest()
    assert main_page.button_home.is_displayed()

