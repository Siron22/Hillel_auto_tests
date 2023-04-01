from requests import Session

from project_files.utilities.useful_func import get_base_api_url


class ExpensesEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() +'/expenses'
        self.session = session

