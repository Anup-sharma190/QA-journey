from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time
from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)# this will pop up a window and display country after enter ind
countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

#print(driver.find_element(By.ID,"autosuggest").text)
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
#assert(driver.find_element(By.ID,"autosuggest").get_attribute("value")== "india"
assert(driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India")

print("ALL DONE")









time.sleep(90)

# Wait for testing

