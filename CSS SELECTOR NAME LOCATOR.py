# //tagname[@attribute="value]
#//input[@type="submit"]#this is custom xpath
import click
import driver
#from selenium.webdriver.chrome import webdriver
#from selenium.webdriver.common.by import By
#from pyexpat.errors import messages
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#print(driver.title)
#print(driver.current_url)
#time.sleep(5)
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
#driver.find_element(By.ID,"exampleCheck1").click()
#driver.find_element(By.XPATH, "//input[@type= "submit"]").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("rahul") # CSS PATH CONSTRUCTION #id is also call css & .classname
driver.find_element(By.XPATH, "//input[@type='submit']").click()# for XPATH CONSTRUCTION
#message= driver.find_element(By.CLASS_NAME,"alert-success").text
#print(message)
#assert "success123" in messages

time.sleep(90)
