import allure
from pytest_check import check


@allure.title('Get current user')
def test_current_user(users_ep, auth_ep, registered_user_api):
    login = auth_ep.sign_in(registered_user_api.email, registered_user_api.password)
    cookies = login.cookies
    response = users_ep.get_users_current(cookies=cookies)
    check.equal(response.status_code, 200)
    """Tear down. Log out"""
    auth_ep.log_out()


@allure.title('Delete user')
def test_current_user(users_ep, auth_ep, unregistered_user_api):
    login = auth_ep.sign_in(unregistered_user_api.email, unregistered_user_api.password)
    # cookies = login.cookies
    # response = users_ep.get_users_current(cookies=cookies)
    # check.equal(response.status_code, 200)
    """Tear down. Log out"""
    users_ep.delete_user()


