import allure
import requests
from api_tests_v2.sources.config_parcer import get_base_api_url


class UsersEndpoint:

    def __init__(self):
        self.url = get_base_api_url() + '/users'

    @allure.step('Gets authenticated user data')
    def get_users_current(self, cookies=None):
        return requests.get(self.url + '/current', cookies=cookies)

    @allure.step('Gets authenticated user profile data')
    def get_users_profile(self, cookies=None):
        return requests.get(self.url + '/profile', cookies=cookies)

    @allure.step('Edits user profile')
    def edit_user_profile(self, name='', photo='', last_name='', date_birth='', country='', cookies=None):
        json = {
            "photo": photo,
            "name": name,
            "lastName": last_name,
            "dateBirth": date_birth,
            "country": country
        }
        return requests.put(self.url + '/profile', json=json, cookies=cookies)

    @allure.step('Gets authenticated user settings data')
    def get_users_setting(self, cookies=None):
        return requests.get(self.url + '/settings', cookies=cookies)

    @allure.step('Edits user settings')
    def edit_user_setting(self, currency="usd", distance_units="km", cookies=None):
        json = {
            "currency": currency,
            "distanceUnits": distance_units
        }
        return requests.put(self.url + '/profile', json, cookies=cookies)

    @allure.step('Changes user email')
    def change_user_email(self, email: str, password: str, cookies=None):
        json = {
            "email": email,
            "password": password
        }
        return requests.put(self.url + '/email', json=json, cookies=cookies)

    @allure.step('Changes user password')
    def change_user_password(self, old_password: str, new_password: str, cookies=None):
        json = {
            "oldPassword": old_password,
            "password": new_password,
            "repeatPassword": new_password
        }
        return requests.put(self.url + '/password', json=json, cookies=cookies)

    @allure.step('Deletes user account and current user session')
    def delete_user(self, cookies=None):
        return requests.delete(self.url, cookies=cookies)


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
