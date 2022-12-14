from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")

time.sleep(5)
driver.find_element_by_name("user-name").send_keys("standard_user")
driver.find_element_by_name("password").send_keys("secret_sauce")
driver.find_element_by_name("login-button").click()
time.sleep(2)