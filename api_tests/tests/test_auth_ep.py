import allure
from pytest_check import check


@allure.title('Logout request')
def test_logout(auth_ep):
    response = auth_ep.log_out()
    value = {
        "status": "ok"
    }
    assert response.status_code == 200
    check.equal(response.json(), value)


@allure.title('Signup request')
def test_sign_up(auth_ep, users_ep, unregistered_user_api):
    response = auth_ep.sign_up(unregistered_user_api.name, unregistered_user_api.lastname,
                               unregistered_user_api.email, unregistered_user_api.password)
    """ Response example
   {
    "status": "ok",
    "data": {
    "userId": 1,
    "distanceUnits": "km",
    "currency": "usd"
      }
    } 
    """
    assert response.status_code == 201
    check.equal(response.json()["status"], "ok")
    check.equal(response.json()["data"]["distanceUnits"], "km")
    check.equal(response.json()["data"]["currency"], "usd")
    """Tear down. Delete user"""
    del_resp = users_ep.delete_user()
    assert del_resp.status_code == 200


@allure.title('Signin request')
def test_sign_in(auth_ep, registered_user_api):
    response = auth_ep.sign_in(registered_user_api.email, registered_user_api.password)
    value = {
        "status": "ok",
        "data": {
            "userId": 32358,
            "distanceUnits": "km",
            "currency": "usd"
        }
    }
    assert response.status_code == 200
    check.equal(response.json(), value)
    """Tear down. Log out"""
    auth_ep.log_out()


@allure.title('Reset password request')
def test_reset_password(auth_ep, users_ep, registered_user_api):
    auth_ep.sign_in(registered_user_api.email, registered_user_api.password)
    response = auth_ep.reset_password('test_mail@mail.com')
    assert response.status_code == 200
    check.equal(response.json()["status"], "ok")
    """Tear down. Log out"""
    auth_ep.log_out()

# TODO: Verify email list sent
