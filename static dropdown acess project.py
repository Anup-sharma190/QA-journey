from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Enter name
driver.find_element(By.NAME, "name").send_keys("Anup")

# Enter email
driver.find_element(By.NAME, "email").send_keys("anupcg06433@gmail.com")

# Enter password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")

# Select gender from dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# Wait for testing
time.sleep(90)
