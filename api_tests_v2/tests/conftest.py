import json
import random
import allure
import pytest
from randomuser import RandomUser

from api_tests_v2.endpoints.ep_auth import AuthEndpoint
from api_tests_v2.endpoints.ep_cars import CarsEndpoint
from api_tests_v2.endpoints.ep_expenses import ExpensesEndpoint
from api_tests_v2.endpoints.ep_instructions import InstructionsEndpoint
from api_tests_v2.endpoints.ep_users import UsersEndpoint
from api_tests_v2.instances.user import User


@pytest.fixture()
def auth_ep():
    return AuthEndpoint()


@pytest.fixture()
def users_ep():
    return UsersEndpoint()


@pytest.fixture()
def cars_ep():
    return CarsEndpoint()


@pytest.fixture()
def expenses_ep():
    return ExpensesEndpoint()


@pytest.fixture()
def instructions_ep():
    return InstructionsEndpoint()


@pytest.fixture()
def registered_user_api():
    return User(name="Anne", lastname="Beatty", email="Etha_Lind@gmail.com", password="Sunday1XxXx", user_id=32358)

@pytest.fixture(scope='session')
def unregistered_user_api():
    return User(name='Andreas', lastname='Niolass', email='Sha.Windl@gmail.com', password='Wednesday5XxXx')


# @allure.step('Prepare user`s data')
# @pytest.fixture()
# def user_with_random_data():
#     randomuser = RandomUser()
#     name = randomuser.get_full_name()
#     email = randomuser.get_email()
#     gender = randomuser.get_gender()
#     status = random.choice(['active', 'inactive'])
#     data = User(name, email, gender, status)
#     return json.dumps(data)



