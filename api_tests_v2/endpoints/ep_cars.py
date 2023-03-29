import allure
import requests
from api_tests_v2.sources.config_parcer import get_base_api_url


class CarsEndpoint:

    def __init__(self):
        self.url = get_base_api_url() +'/cars'


    @allure.step('Gets car brands')
    def get_car_brands(self):
        url = self.url+'/brands'
        return requests.get(url)


    @allure.step('Gets car brand by id')
    def get_car_brand_by_id(self, brand_id:int):
        url = self.url + '/brands' + f'/{brand_id}'
        return requests.get(url)


    @allure.step('Gets car models')
    def get_car_models(self):
        url = self.url + '/models'
        return requests.get(url)


    @allure.step('Gets car model by id')
    def get_car_model_by_id(self, model_id):
        url = self.url + '/models'+ f'/{model_id}'
        return requests.get(url)


    @allure.step('Gets current user cars')
    def get_user_cars(self):
        return requests.get(self.url)


    @allure.step('Gets current user cars')
    def create_new_car(self, car_brand_id:int, car_model_id:int, mileage:int):
        json = {
                  "carBrandId": car_brand_id,
                  "carModelId": car_model_id,
                  "mileage": mileage
                }
        return requests.post(self.url, json=json)


    @allure.step('Gets current user car by id')
    def get_user_car_by_id(self, car_id: int):
        url = self.url + '/models' + f'/{car_id}'
        return requests.get(url)


    @allure.step('Edit existing car')
    def edit_user_car(self, car_id: int, car_brand_id:int, car_model_id:int, mileage:int):
        url = self.url + '/models' + f'/{car_id}'
        json = {
                  "carBrandId": car_brand_id,
                  "carModelId": car_model_id,
                  "mileage": mileage
                }
        return requests.post(url, json=json)


    @allure.step('Delete user car by id')
    def get_user_car_by_id(self, car_id: int):
        url = self.url + '/models' + f'/{car_id}'
        return requests.delete(url)

