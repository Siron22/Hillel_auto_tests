import allure
import requests
from api_tests_v2.sources.config_parcer import get_base_api_url


class ExpensesEndpoint:

    def __init__(self):
        self.url = get_base_api_url() +'/expenses'