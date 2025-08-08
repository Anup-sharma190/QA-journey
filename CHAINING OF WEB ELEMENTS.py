from pydoc import text

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Type 'ber' to filter some products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # Let products load

# Get list of all filtered products
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Click only the FIRST product's button
#results[0].find_element(By.XPATH, "div/button").click() THIS TO CLICK ANY PATICULAR BY MENTIONING INDEX
for result in results:
    result.find_element(By.XPATH,"div/button").click()# this will click all 3
# new method
#if you want to add paticular 3 rd number only
#results[2].find_element(By.XPATH,"div/button").click()
#time.sleep(10)
# to click on cart button
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
#time.sleep(10)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
#time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
#time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
#time.sleep(5)
print("order placed")





print("Clicked the first product successfully.")
