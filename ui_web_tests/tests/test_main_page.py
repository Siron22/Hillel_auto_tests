import allure


@allure.title('Main test for main page')
@allure.severity(allure.severity_level.BLOCKER)
def test_main_page_is_open(driver, main_page):
    with allure.step("Verify title"):
        title = driver.title
    assert 'Hillel Qauto' in title


@allure.description('Test for all main paige elements visibility')
def test_main_page_elements_displayed(driver, main_page):
    with allure.step("Choose logo"):
        logo = main_page.logo_hillel_auto
    assert logo.is_displayed()

    with allure.step("Choose button home"):
        button_home = main_page.button_home
    assert button_home.is_displayed()

    with allure.step("Choose button about"):
        button_about = main_page.button_about
    assert button_about.is_displayed()

    """соответственно и так далее если это имеет смысл"""

    assert main_page.button_contacts.is_displayed()
    assert main_page.button_guest_login.is_displayed()
    assert main_page.button_signin.is_displayed()
    assert main_page.button_signup.is_displayed()
    assert main_page.string1.is_displayed()
    assert main_page.string2.is_displayed()


@allure.issue('http://jira.com', name='BUG-X3')
def test_main_page_video_displayed(driver, main_page):
    """Визуально объект присутствует, а тест почему-то падает"""
    assert main_page.video_locator.is_displayed()

# TODO: Make launch video test
