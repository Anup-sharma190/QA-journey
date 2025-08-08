import time


from  selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#driver.webdriver.chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
results= driver.find_elements(By.XPATH,"//div[@class='products']/div")
count= len(results)
print(count)
#assert count >
#...........................
#for result in results:
    #result.find_element(By.XPATH,"div/button").click()



