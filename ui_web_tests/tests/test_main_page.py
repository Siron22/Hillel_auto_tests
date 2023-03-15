import allure
import pytest


@allure.title('Main test for main page')
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_is_open(driver, main_page):
    with allure.step("Verify title"):
        assert 'Hillel Qauto' in driver.title


@allure.description('Test for all main paige elements visibility')
def test_main_page_elements_displayed(driver, main_page):
    #assert main_page.video_locator.is_displayed()
    assert main_page.logo_hillel_auto.is_displayed()
    assert main_page.button_home.is_displayed()
    assert main_page.button_about.is_displayed()
    assert main_page.button_contacts.is_displayed()
    assert main_page.button_guest_login.is_displayed()
    assert main_page.button_signin.is_displayed()
    assert main_page.button_signup.is_displayed()
    assert main_page.string1.is_displayed()
    assert main_page.string2.is_displayed()


@allure.title('Test for main page video')
def test_main_page_video_displayed(driver, main_page):
    assert main_page.video.is_displayed()


@allure.title('Test for main page facebook link')
def test_main_page_facebook_link_is_open(driver, main_page):
    main_page.click_icon_facebook()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://www.facebook.com/Hillel.IT.School'


@allure.title('Test for main page telegram link')
def test_main_page_telegram_link_is_open(driver, main_page):
    main_page.click_icon_telegram()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://t.me/ithillel_kyiv'


@allure.title('Test for main page youtube link')
def test_main_page_youtube_link_is_open(driver, main_page):
    main_page.click_icon_youtube()
    driver.switch_to.window(driver.window_handles[1])
    import time
    time.sleep(3)
    assert driver.current_url == 'https://www.youtube.com/user/HillelITSchool'

@pytest.mark.xfail("test failed while authentification in LinkedIn is required")
@allure.title('Test for main page instagram link')
def test_main_page_instagram_link_is_open(driver, main_page):
    main_page.click_icon_instagram()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://www.instagram.com/hillel_itschool/'


@pytest.mark.xfail("test failed while authentification in LinkedIn is required")
@allure.title('Test for main page linkedIn link')
def test_main_page_linkedin_link_is_open(driver, main_page):
    """test failed while authentification in LinkedIn is required"""
    main_page.click_icon_linkedin()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://www.linkedin.com/school/ithillel/'



"""
Not tests!!!
Only features verify
"""

@allure.title('Scroll the page')
def test_main_page_scroll_to_end(driver, main_page):
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    import time
    time.sleep(2)

@allure.title('Scroll the page')
def test_main_page_click_about(driver, main_page):
    """trial test for the location of the object on the page"""
    import time
    print('Window rect: ', driver.get_window_rect())
    print('Email location: ', main_page.link_email.location)
    print('Link email: ', driver.execute_script("return arguments[0].getBoundingClientRect();", main_page.link_email))  # {'bottom': 1286.09375, 'height': 19, 'left': 1356.671875, 'right': 1506.5, 'toJSON': {}, 'top': 1267.09375, 'width': 149.828125, 'x': 1356.671875, 'y': 1267.09375}
    time.sleep(1)
    main_page.click_button_about()
    time.sleep(1)
    print('Window rect: ', driver.get_window_rect())
    print('Email location: ',main_page.link_email.location)
    print('Link email: ',driver.execute_script("return arguments[0].getBoundingClientRect();", main_page.link_email))  # {'bottom': 701.09375, 'height': 19, 'left': 1356.671875, 'right': 1506.5, 'toJSON': {}, 'top': 682.09375, 'width': 149.828125, 'x': 1356.671875, 'y': 682.09375}

# @allure.title('Click button "Home"')
# def test_main_page_click_home(driver, main_page):
#     main_page.click_button_home
#
# @allure.title('Click button "Contacts"')
# def test_main_page_click_contacts(driver, main_page):
#     main_page.click_button_contacts

# TODO: Make launch video test

