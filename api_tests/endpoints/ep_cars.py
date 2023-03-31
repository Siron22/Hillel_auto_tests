import allure
import requests
from requests import Session

from api_tests.sources.config_parcer import get_base_api_url


class CarsEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() + '/cars'
        self.session = session

    @allure.step('Gets car brands')
    def get_car_brands(self):
        return self.session.get(self.url + '/brands')

    @allure.step('Gets car brand by id')
    def get_car_brand_by_id(self, brand_id: int):
        return self.session.get(self.url + '/brands' + f'/{brand_id}')

    @allure.step('Gets car models')
    def get_car_models(self):
        return self.session.get(self.url + '/models')

    @allure.step('Gets car model by id')
    def get_car_model_by_id(self, model_id):
        url = self.url + '/models' + f'/{model_id}'
        return self.session.get(url)

    @allure.step('Gets current user cars')
    def get_user_cars(self):
        return self.session.get(self.url)

    @allure.step('Gets current user cars')
    def create_new_car(self, car_brand_id: int, car_model_id: int, mileage: int):
        json = {
            "carBrandId": car_brand_id,
            "carModelId": car_model_id,
            "mileage": mileage
        }
        return self.session.post(self.url, json=json)

    @allure.step('Gets current user car by id')
    def get_user_car_by_id(self, car_id: int):
        return self.session.get(self.url + '/models' + f'/{car_id}')

    @allure.step('Edit existing car')
    def edit_user_car(self, car_id: int, car_brand_id: int, car_model_id: int, mileage: int):
        json = {
            "carBrandId": car_brand_id,
            "carModelId": car_model_id,
            "mileage": mileage
        }
        return self.session.post(self.url + '/models' + f'/{car_id}', json=json)

    @allure.step('Delete user car by id')
    def get_user_car_by_id(self, car_id: int):
        return self.session.delete(self.url + '/models' + f'/{car_id}')
