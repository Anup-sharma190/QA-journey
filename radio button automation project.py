from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()  # ✅ Create Chrome driver object
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH,("//input[@type='checkbox']"))
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
print("all done maska")
#---------------
radioButtons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected# to cr
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not (driver.find_element(By.ID,"displayed-text").is_displayed())# osscheck weather option 2
time.sleep(20)