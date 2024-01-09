# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://bansalsale.com/login")
# driver.maximize_window()
#
# driver.find_element(By.CSS_SELECTOR,  "#loginForm > div:nth-child(1) > input").send_keys("admin@gmail.com")
# driver.find_element(By.ID,  "dz-password").send_keys("Admin@123")
# driver.find_element(By.CSS_SELECTOR,  "#loginForm > div.text-center.mb-4 > button").click()
#
# time.sleep(5)
#





import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,  "/html/body/app-root/app-password-new/div/div/div/div/div[2]/form/div[1]/input").send_keys("kaylejoh@gmail.com")
driver.find_element(By.XPATH,  '//*[@id="userPassword"]').send_keys("63942calcuttA$")
driver.find_element(By.XPATH,  '//*[@id="confirmPassword"]').send_keys("63942calcuttA$")
driver.find_element(By.XPATH,  '/html/body/app-root/app-password-new/div/div/div/div/div[2]/form/div[4]/button').click()

time.sleep(5)

