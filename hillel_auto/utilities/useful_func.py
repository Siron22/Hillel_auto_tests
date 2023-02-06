from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import time





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


def get_browser_name():
    return get_config().get('project', 'browser_name')


def get_screenshot_directory():
    return get_config().get('project', 'screenshot-directory')

a= get_base_url()
print(get_base_url())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.google.com/')
time.sleep(3)
driver.close()