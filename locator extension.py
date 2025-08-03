from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)

driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, " password?").click()# partial text also work will detect full link
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("anupcg06433@gmail.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")
#driver.find_element(By.CSS_SELECTOR, "#confirmpassword").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='confirmPassword']").send_keys("123456")

#driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()



time.sleep(90)