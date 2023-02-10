from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

signin_email = 'Shany.Windler@gmail.com'
signin_password = 'Wednesday1XxXx'

driver.get('https://guest:welcome2qauto@qauto2.forstudy.space/')
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
sign_in_button = driver.find_element(By.XPATH, '//*/div[2]/button[2]').click()
# username_input_field = driver.find_element(By.ID, 'signinEmail').send_keys(signin_email)
# password_input_field = driver.find_element(By.ID, 'signinPassword').send_keys(signin_password)
# login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary:nth-child(2)').click()


time.sleep(3)
driver.close()
