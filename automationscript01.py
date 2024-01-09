from selenium import webdriver
from selenium.webdriver.chrome.service import Service



service_obj = Service()
driver = webdriver.Chrome(service=service_obj)   ###--------------for firfox browser use gecko driver path and for edge use msedgedriver----------------- ###
driver.get("https://bansalsale.com/login")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.forward()
driver.refresh()
driver.back()
driver.minimize_window()

driver.close()

