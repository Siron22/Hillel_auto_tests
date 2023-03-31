import allure
import requests
from requests import Session

from api_tests_v2.sources.config_parcer import get_base_api_url


class AuthEndpoint:


    def __init__(self, session: Session):
        self.url = get_base_api_url()+'/auth'
        self.session = session


    @allure.step('Ends up user session. Clears session cookies.')
    def log_out(self):
        url = self.url+'/logout'
        return self.session.get(url)


    @allure.step('Registers users in the system.')
    def sign_up(self, name, last_name, email, password):
        url = self.url+'/signup'
        json = {
                  "name": name,
                  "lastName": last_name,
                  "email": email,
                  "password": password,
                  "repeatPassword": password
                }
        return self.session.post(url, json=json)


    @allure.step('Registered user login in the system.')
    def sign_in(self, email, password, remember=False):
        url = self.url+'/signin'
        json = {
                  "email": email,
                  "password": password,
                  "remember": remember
                }
        return self.session.post(url, json=json)


    @allure.step('Reset password')
    def reset_password(self, email):
        url = self.url + '/resetPassword'
        json = {
                "email": email
            }
        return self.session.post(url, json=json)






"""Client test code"""
# a = AuthEndpoint()
# response = a.sign_in("Etha_Lind@gmail.com", "Sunday1XxXx")
# print('Response: ', response)
# print('-s'*100)
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
#
# response = a.log_out()
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