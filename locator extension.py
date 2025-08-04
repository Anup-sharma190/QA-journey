from select import select
from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com/client")
#driver.maximize_window()
#print(driver.title)
#print(driver.current_url)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.find_element(By.LINK_TEXT, "Forgot password?").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, " password?").click()# partial text also work will detect full link
#driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("anupcg06433@gmail.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456")
#driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("123456")
#driver.find_element(By.CSS_SELECTOR, "#confirmpassword").send_keys("123456")
#driver.find_element(By.CSS_SELECTOR, "input[formcontrolname='confirmPassword']").send_keys("123456")

#driver.find_element(By.XPATH, "//button[@type='submit']").click()
#driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
#STATIC DROPDOWN
dropdown= Select(driver.find_element(By.ID,"examplefor controldelect1"))
dropdown.select_by_index(0)# you can select by index start from 0
dropdown.select_by_visible_text("Female")# you can select by visible text also
#dropdown.select_by_value() you can select any value also from the attibutes if it is declared on inspect html page






time.sleep(90)