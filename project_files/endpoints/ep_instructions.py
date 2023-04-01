from requests import Session

from project_files.utilities.useful_func import get_base_api_url


class InstructionsEndpoint:

    def __init__(self, session: Session):
        self.url = get_base_api_url() + '/instructions'
        self.session = session
