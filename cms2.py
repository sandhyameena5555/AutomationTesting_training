import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bansalsale.com/")

username_field = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/input')
password_field = driver.find_element(By.XPATH, '//*[@id="dz-password"]')
submit_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[4]/button')

username_field.send_keys('sandhya@email.com')
password_field.send_keys('Sandhya123')

print("login credentials")
print("username=sandhya@email.com")
print("password=Sandhya123")

driver.maximize_window()




submit_button.click()

driver.implicitly_wait(5)

time.sleep(10)
driver.close()