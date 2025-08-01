import time

#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

# chrome driver service which invoke chrome here
#service_obj= Service("C:\Users\Comp10\Downloads\chromedriver.exe")
#service_obj = Service("C:\\Users\\Comp10\\Downloads\\chromedriver.exe")
#C:\Users\Comp10\Downloads\chromedriver-win64
# selinium see the path and get driver service
#driver= webdriver.Chrome(service= service_obj)
#driver= webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com")
#time.sleep(10)
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service

#service = Service(r"C:\Users\Comp10\Downloads\chromedriver.exe")
#driver = webdriver.Chrome(service=service)
#driver.get("https://google.com")
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options

# Safe path formatting
#service = Service(r"C:\chromedriver\chromedriver.exe")  # use the correct extracted path

#options = Options()
#driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://www.google.com")
from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(5)

