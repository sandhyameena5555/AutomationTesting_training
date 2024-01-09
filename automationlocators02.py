import time
from calendar import calendar

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
######-------------ID , XPATH, CSSSelector , Classname, NAME, linkText ----------------#############
driver.find_element(By.NAME, "email").send_keys("Admin@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Admin123#")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Admin")
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/input" ).click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text    #####------- after every space there is an one diffrent class for particular element------#######
print(message)
assert "success" in message
driver.find_element(By.ID, "inlineRadio1").click()
driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/h4/input").send_keys("Adminagain")
driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/h4/input").clear()
dropdown = driver.find_element(By.ID, "exampleFormControlSelect1")
select = Select(dropdown)

select.select_by_visible_text("Female")
date_picker = driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[7]/input" )
date_picker.clear()
date_picker.send_keys("12-09-2024")


time.sleep(5)


