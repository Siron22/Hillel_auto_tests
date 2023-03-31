import allure
import requests
from requests import Session

from api_tests.sources.config_parcer import get_base_api_url


class ExpensesEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() +'/expenses'
        self.session = session

