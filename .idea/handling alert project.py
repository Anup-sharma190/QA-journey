from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
name = "rahul"
driver = webdriver.Chrome()  # ✅ Create Chrome driver object
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alerttext= alert.text
print(alerttext)
assert name in alerttext
alert.accept()#to select
#alert.dismiss()# to cancell

time.sleep(20)
#alert.dismiss#to cancel on page
