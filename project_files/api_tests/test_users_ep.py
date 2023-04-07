import allure
import pytest
from pytest_check import check

from project_files.instances.user import UserValidData


@allure.title('Get current user')
def test_get_current_user(users_ep, auth_ep, ru_api):
    login = auth_ep.sign_in(ru_api.email, ru_api.password)
    ru_api.get_user_id(login)
    json = {
        "status": "ok",
        "data": {
            "userId": ru_api.user_id,
            "distanceUnits": ru_api.distance_units,
            "currency": ru_api.currency,
            "photoFilename": ru_api.photo_filename
        }
    }
    response = users_ep.get_users_current()
    assert response.status_code == 200
    check.equal(response.json(), json)
    """Tear down. Log out"""
    auth_ep.log_out()


@allure.title('Get users profile')
def test_get_users_profile(users_ep, auth_ep, ru_api):
    login = auth_ep.sign_in(ru_api.email, ru_api.password)
    ru_api.get_user_id(login)
    requirement_json = {
        "status": "ok",
        "data": {
            "userId": ru_api.user_id,
            "photoFilename": ru_api.photo_filename,
            "name": ru_api.name,
            "lastName": ru_api.lastname
        }
    }
    response = users_ep.get_users_profile()
    response_json = response.json()
    assert response.status_code == 200
    check.equal(response_json, requirement_json)
    if response_json != requirement_json:
        check.equal(response_json["status"], "ok")
        check.equal(response_json["data"]["userId"], ru_api.user_id)
        check.equal(response_json["data"]["photoFilename"], ru_api.photo_filename)
        check.equal(response_json["data"]["name"], ru_api.name)
        check.equal(response_json["data"]["lastName"], ru_api.lastname)
    """Tear down. Log out"""
    auth_ep.log_out()


@allure.title('Get users profile')
def test_edit_users_profile(users_ep, auth_ep, eu_api):
    auth_ep.sign_in(eu_api.email, eu_api.password)
    """This  request require to set birthday date in valid format, all other field can be empty"""
    response = users_ep.edit_user_profile(name="Ivan", last_name="Revenko",
                                          date_birth="1999-08-03T19:20:07.000Z", country="Ukraine")
    assert response.status_code == 200
    check.equal(response.json()["status"], "ok")
    check.equal(response.json()["data"]["userId"], eu_api.user_id)
    check.equal(response.json()["data"]["name"], "Ivan")
    check.equal(response.json()["data"]["lastName"], "Revenko")
    check.equal(response.json()["data"]["dateBirth"], "1999-08-03T19:20:07.000Z")
    check.equal(response.json()["data"]["country"], "Ukraine")
    """Tear down. Set defaults and log out"""
    users_ep.edit_user_profile(name=eu_api.name, last_name=eu_api.lastname, date_birth="1888-12-12T19:20:07.000Z",
                               country="")
    auth_ep.log_out()


@allure.title('Get users settings')
def test_get_users_settings(users_ep, auth_ep, ru_api, teardown_logout):
    auth_ep.sign_in(ru_api.email, ru_api.password)
    response = users_ep.get_users_setting()
    requirement_json = {
        "status": "ok",
        "data": {
            "currency": "us",
            "distanceUnits": "km"
        }
    }
    response_json = response.json()
    assert response.status_code == 200
    check.equal(response_json, requirement_json)
    if response_json != requirement_json:
        check.equal(response_json["status"], "ok")
        check.equal(response_json["data"]["currency"], ru_api.currency)
        check.equal(response_json["data"]["distanceUnits"], ru_api.distance_units)
    """Tear down. Log out"""
    auth_ep.log_out()


@pytest.mark.parametrize('currency', UserValidData.CURRENCY)
@allure.title('Edit users settings: currency')
def test_edit_users_settings_cur(users_ep, auth_ep, ru_api, currency):
    auth_ep.sign_in(ru_api.email, ru_api.password)
    requirement_json = {
        "status": "ok",
        "data": {
            "currency": currency,
            "distanceUnits": "km"
        }
    }
    response = users_ep.edit_user_setting(currency=currency)
    response_json = response.json()
    assert response.status_code == 200
    check.equal(response_json, requirement_json)
    if response_json != requirement_json:
        check.equal(response_json["status"], "ok")
        check.equal(response_json["data"]["currency"], currency)
        check.equal(response_json["data"]["distanceUnits"], ru_api.distance_units)
    """Tear down. Default settings and log out"""
    users_ep.edit_user_setting()
    auth_ep.log_out()


@pytest.mark.parametrize('distance_units', UserValidData.DISTANCE_UNITS)
@allure.title('Edit users settings: distance units')
def test_edit_users_settings_dist(users_ep, auth_ep, ru_api, distance_units):
    auth_ep.sign_in(ru_api.email, ru_api.password)
    requirement_json = {
        "status": "ok",
        "data": {
            "currency": "usd",
            "distanceUnits": distance_units
        }
    }
    response = users_ep.edit_user_setting(distance_units=distance_units)
    response_json = response.json()
    assert response.status_code == 200
    check.equal(response_json, requirement_json)
    if response_json != requirement_json:
        check.equal(response_json["status"], "ok")
        check.equal(response_json["data"]["currency"], "usd")
        check.equal(response_json["data"]["distanceUnits"], distance_units)
    """Tear down. Default settings and log out"""

    users_ep.edit_user_setting()
    auth_ep.log_out()


# @allure.title('Delete user')
# def test_delete_current_user(users_ep, auth_ep, uu_api):
#     auth_ep.sign_in(uu_api.email, uu_api.password)
#     """Tear down. Log out"""
#     users_ep.delete_user()


