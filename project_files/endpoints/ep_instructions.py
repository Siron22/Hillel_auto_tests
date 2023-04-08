import allure
from requests import Session
from project_files.utilities.useful_func import get_base_api_url


class InstructionsEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() + '/instructions'
        self.session = session

    @allure.step('Get all instructions')
    def get_all_instructions(self):
        return self.session.get(self.url)

    @allure.step('Get an instruction by id')
    def get_expense_by_id(self, instr_id: int):
        return self.session.get(self.url + f'/{instr_id}')
