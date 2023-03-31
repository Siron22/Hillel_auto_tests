import allure
import requests
from requests import Session
from api_tests.sources.config_parcer import get_base_api_url


class UsersEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() + '/users'
        self.session = session

    @allure.step('Gets authenticated user data')
    def get_users_current(self):
        return self.session.get(self.url + '/current')

    @allure.step('Gets authenticated user profile data')
    def get_users_profile(self, cookies=None):
        return self.session.get(self.url + '/profile')

    @allure.step('Edits user profile')
    def edit_user_profile(self, name='', photo='', last_name='', date_birth='', country=''):
        json = {
            "photo": photo,
            "name": name,
            "lastName": last_name,
            "dateBirth": date_birth,
            "country": country
        }
        return self.session.put(self.url + '/profile', json=json)

    @allure.step('Gets authenticated user settings data')
    def get_users_setting(self, cookies=None):
        return self.session.get(self.url + '/settings')

    @allure.step('Edits user settings')
    def edit_user_setting(self, currency="usd", distance_units="km"):
        json = {
            "currency": currency,
            "distanceUnits": distance_units
        }
        return self.session.put(self.url + '/profile', json)

    @allure.step('Changes user email')
    def change_user_email(self, email: str, password: str):
        json = {
            "email": email,
            "password": password
        }
        return self.session.put(self.url + '/email', json=json)

    @allure.step('Changes user password')
    def change_user_password(self, old_password: str, new_password: str):
        json = {
            "oldPassword": old_password,
            "password": new_password,
            "repeatPassword": new_password
        }
        return self.session.put(self.url + '/password', json=json)

    @allure.step('Deletes user account and current user session')
    def delete_user(self, cookies=None):
        return self.session.delete(self.url)


"""Client test code"""
# a = UsersEndpoint()
# response = a.get_users_profile()
# print('Response: ', response)
# print('-'*100)
# print('Status code: ', response.status_code)
# print('-'*100)
# print('Json: ', response.json())
# print('-'*100)
# print('Text: ', response.text)
# print('-'*100)
# print('Content: ', response.content)
# print('-'*100)
# print('Headers: ', response.headers)
# print('-'*100)
# print('Cookies: ', response.cookies)
# print('-'*100)
