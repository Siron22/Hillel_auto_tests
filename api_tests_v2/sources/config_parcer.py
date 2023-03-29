from configparser import ConfigParser
import os

def get_base_api_url():
    root_dir = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    config = ConfigParser()
    config.read(os.path.join(root_dir, 'config.ini'))
    return config.get('project', 'base_api_url')

