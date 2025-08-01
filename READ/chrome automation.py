from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"C:\Users\Comp10\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

# Enter login details
driver.find_element("id", "username").send_keys("rahul")
driver.find_element("id", "password").send_keys("learning")
driver.find_element("id", "signInBtn").click()
