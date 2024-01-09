# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
#
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print(len(checkboxes))
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") =="option2":         ##################--------------this method is specially selected that checkbox which we want ---------------######
#         checkbox.click()
#         assert checkbox.is_selected()          ###########------------that line don't know but it work for selected the checkbox it's optional----------------###########
#         break
#
# time.sleep(5)





import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") =="radio3":
        checkbox.click()
        break


assert driver.find_element(By.ID, "displayed-text").is_displayed()                  #####--------is.displayed is basically for hide button show b utton click purpose----###
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()



time.sleep(5)


