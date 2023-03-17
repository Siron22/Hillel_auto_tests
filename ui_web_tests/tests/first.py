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
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
video = driver.find_element(By.CSS_SELECTOR, '.ytp-large-play-button')
movie_player = driver.find_element(By.ID, 'movie_player')
video.click()
print('Start:', movie_player.get_attribute("class"))
time.sleep(3)
print('Play:', movie_player.get_attribute("class"))
movie_player.click()
print('Pause:', movie_player.get_attribute("class"))



# driver.find_element(By.CSS_SELECTOR, '.icon-youtube').click()
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH, '//span[text()="Reject all"]').click()
#############################################
# print(driver.title)
# sign_in_button = driver.find_element(By.XPATH, '//*/div[2]/button[2]').click()
# username_input_field = driver.find_element(By.ID, 'signinEmail').send_keys(signin_email)
# password_input_field = driver.find_element(By.ID, 'signinPassword').send_keys(signin_password)
# login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-primary:nth-child(2)').click()
#
driver.close()
