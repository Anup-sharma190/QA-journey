from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# Actions
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("rahul")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # Correct CSS for ID

# Optional: print success message
message = driver.find_element(By.CLASS_NAME, "alert-success").text# learn how to grab text
print("Message:", message)

# Keep browser open for 90 seconds to observe

#driver.quit()
driver.find_element(By.XPATH,"(//input[@type='text'] ) [3]").send_keys("don")# learn how to write data
driver.find_element(By.XPATH,"(//input[@type='text'] ) [2]").clear()#learn how to clee
text_fields = driver.find_elements(By.XPATH, "//input[@type='text']")
# to cleer all fields of above inpute
for field in text_fields:
    field.clear()
# r all data


time.sleep(90)