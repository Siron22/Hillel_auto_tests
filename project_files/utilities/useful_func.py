from configparser import ConfigParser
import os


def get_root_directory():
    return os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]


def get_config():
    config = ConfigParser()
    config.read(os.path.join(get_root_directory(), 'config.ini'))
    return config


def get_base_url():
    return get_config().get('project', 'base_url')


def get_base_api_url():
    root_dir = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    config = ConfigParser()
    config.read(os.path.join(root_dir, 'config.ini'))
    return config.get('project', 'base_api_url')


def get_browser_name():
    return get_config().get('project', 'browser_name')


def get_screenshot_directory():
    screen_dir = get_config().get('project', 'screenshot-directory')
    return os.path.join(get_root_directory(), screen_dir)
