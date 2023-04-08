import allure
from requests import Session
from project_files.utilities.useful_func import get_base_api_url


class ExpensesEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() + '/expenses'
        self.session = session

    @allure.step('Get all expenses')
    def get_all_expenses(self):
        return self.session.get(self.url)

    @allure.step('Create an expense')
    def create_an_expense(self, car_id=None, reported_at=None, mileage=None, liters=None, total_cost=None):
        json = {
            "carId": car_id,
            "reportedAt": reported_at,
            "mileage": mileage,
            "liters": liters,
            "totalCost": total_cost,
            "forceMileage": False
        }
        return self.session.post(self.url, json=json)

    @allure.step('Get an expense by id')
    def get_expense_by_id(self, exp_id: int):
        return self.session.get(self.url + f'/{exp_id}')

    @allure.step('Edit an expense')
    def edit_an_expense(self, exp_id=None, car_id=None, reported_at=None, mileage=None, liters=None, total_cost=None):
        json = {
            "carId": car_id,
            "reportedAt": reported_at,
            "mileage": mileage,
            "liters": liters,
            "totalCost": total_cost,
            "forceMileage": False
        }
        return self.session.put(self.url + f'/{exp_id}', json=json)

    @allure.step('Remove an expense')
    def delete_expense_by_id(self, exp_id: int):
        return self.session.delete(self.url + f'/{exp_id}')
