from pydoc import text

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
expectedlist = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actuallist = []  #

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Type 'ber' to filter some products
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(15)  # Let products load

# Get list of all filtered products
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

# Click only the FIRST product's button
#results[0].find_element(By.XPATH, "div/button").click() THIS TO CLICK ANY PATICULAR BY MENTIONING INDEX
for result in results:
    actuallist.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH,"div/button").click()# this will click all 3

assert expectedlist == actuallist
print(actuallist)

# new method
#if you want to add paticular 3 rd number only
#results[2].find_element(By.XPATH,"div/button").click()
#time.sleep(10)
# to click on cart button
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

time.sleep(10)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)
prices= driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")# plural case of elements word to use
sum= 0
for price in prices:
    sum = sum+int(price.text)# 48 it itegrates through each loop and help us to sum,price.text if you want to extract
print(sum)
total_amount= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == total_amount

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("rahulshettyacademy")
#time.sleep(5)# to enter and click this time.sleep not required but to
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
#print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
#time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
#time.sleep(5)
print("order placed")





print("Clicked the first product successfully.")

