import pytest


def test_main_page_is_open(driver, main_page):
    assert 'Hillel Qauto' in driver.title


def test_main_page_elements_displayed(driver, main_page):
    assert main_page.logo_hillel_auto.is_displayed()
    assert main_page.button_home.is_displayed()
    assert main_page.button_about.is_displayed()
    assert main_page.button_contacts.is_displayed()
    assert main_page.button_guest_login.is_displayed()
    assert main_page.button_signin.is_displayed()
    assert main_page.button_signup.is_displayed()
    assert main_page.string1.is_displayed()
    assert main_page.string2.is_displayed()

def test_main_page_video_displayed(driver, main_page):
    """Визуально объект присутствует, а тест почему-то падает"""
    assert main_page.video_locator.is_displayed()

# TODO: Make launch video test
