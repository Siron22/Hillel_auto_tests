import allure
from pytest_check import check
from selenium.webdriver.common.by import By
import time


@allure.title('Main test for main page')
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_is_open(driver, main_page):
    with allure.step("Verify title"):
        assert 'Hillel Qauto' in driver.title


@allure.description('Test for all main paige elements visibility')
def test_main_page_elements_displayed(driver, main_page):
    check.is_true(main_page.element_is_visible(main_page.LOGO_HILLEL_AUTO_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_HOME_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_ABOUT_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_CONTACTS_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_SIGNIN_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_SIGNUP_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.BUTTON_GUEST_LOGIN_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.STRING1_LOCATOR))
    check.is_true(main_page.element_is_visible(main_page.STRING2_LOCATOR))


@allure.description('Test for texts on main page')
def test_main_page_text_on_main(driver, main_page):
    assert main_page.string1.text == "Do more!"
    assert main_page.string2.text == "With the help of the Hillel auto project, you will have the opportunity " \
                                     "to get hands-on experience in manual testing."



@allure.title('Test for main page video')
def test_main_page_video_displayed(driver, main_page):
    assert main_page.element_is_visible(main_page.VIDEO_LOCATOR)


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
    driver.find_element(By.XPATH, '//span[text()="Reject all"]').click()
    assert driver.current_url == 'https://www.youtube.com/user/HillelITSchool'


@allure.title('Test for main page instagram link')
def test_main_page_instagram_link_is_open(driver, main_page):
    main_page.click_icon_instagram()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://www.instagram.com/hillel_itschool/'


@allure.title('Test for main page linkedIn link')
def test_main_page_linkedin_link_is_open(driver, main_page):
    """test failed while authentification in LinkedIn is required"""
    main_page.click_icon_linkedin()
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == 'https://www.linkedin.com/school/ithillel/'


"""Test for movie player"""

@allure.title('Test movie player is ready to use')
def test_main_page_movie_player_is_ready(driver, main_page):
    main_page.video.click()
    """This parameter is taking directly after button "Play" click and before 
    the video starts to play"""
    player_mode = main_page.movie_player.get_attribute("class")
    assert 'unstarted-mode' in player_mode


@allure.title('Test video is playing')
def test_main_page_movie_player_is_launch(driver, main_page):
    main_page.video.click()
    time.sleep(1)
    player_mode = main_page.movie_player.get_attribute("class")
    assert 'playing-mode' in player_mode


@allure.title('Test video is paused')
def test_main_page_movie_player_is_paused(driver, main_page):
    main_page.video.click()
    time.sleep(1)
    main_page.movie_player.click()
    player_mode = main_page.movie_player.get_attribute("class")
    assert 'pause-overlay' in player_mode


""" Not tests!!! Only features verify """

@allure.title('Scroll the page')
def test_main_page_scroll_to_end(driver, main_page):
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    time.sleep(1)

@allure.title('Scroll the page')
def test_main_page_click_about(driver, main_page):
    """trial test for the location of the object on the page"""
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
#     main_page.click_button_contact



