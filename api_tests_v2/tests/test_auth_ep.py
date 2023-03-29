import allure


@allure.title('Logout request')
def test_logout(auth_ep):
    response = auth_ep.log_out()
    assert response.status_code == 400