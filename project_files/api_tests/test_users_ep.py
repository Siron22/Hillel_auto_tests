import allure
from pytest_check import check


@allure.title('Get current user')
def test_get_current_user(users_ep, auth_ep, ru_api):
    auth_ep.sign_in(ru_api.email, ru_api.password)
    response = users_ep.get_users_current()
    assert response.status_code == 200
    """Tear down. Log out"""
    auth_ep.log_out()


# @allure.title('Delete user')
# def test_delete_current_user(users_ep, auth_ep, uu_api):
#     auth_ep.sign_in(uu_api.email, uu_api.password)
#     """Tear down. Log out"""
#     users_ep.delete_user()


