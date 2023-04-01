import pytest
import requests
from project_files.endpoints.ep_auth import AuthEndpoint
from project_files.endpoints.ep_cars import CarsEndpoint
from project_files.endpoints.ep_expenses import ExpensesEndpoint
from project_files.endpoints.ep_instructions import InstructionsEndpoint
from project_files.endpoints.ep_users import UsersEndpoint
from project_files.instances.user import User


@pytest.fixture()
def session():
    with requests.Session() as session:
        yield session


"""Second workable variant for this fixture"""


# @pytest.fixture()
# def session():
#     session = requests.Session()
#     yield session
#     session.close()


@pytest.fixture()
def auth_ep(session):
    yield AuthEndpoint(session)


@pytest.fixture()
def users_ep(session):
    yield UsersEndpoint(session)


@pytest.fixture()
def cars_ep(session):
    yield CarsEndpoint(session)


@pytest.fixture()
def expenses_ep(session):
    yield ExpensesEndpoint(session)


@pytest.fixture()
def instructions_ep(session):
    yield InstructionsEndpoint(session)


@pytest.fixture(name='ru_api')
def registered_user_api():
    yield User(name="Anne", lastname="Beatty", email="Etha_Lind@gmail.com", password="Sunday1XxXx", user_id=32358)


@pytest.fixture(name='uu_api')
def unregistered_user_api():
    yield User(name='Andreas', lastname='Niolass', email='Sha.Windl@gmail.com', password='Wednesday5XxXx')

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
