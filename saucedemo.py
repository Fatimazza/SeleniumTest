import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #each function begin with "test" and run alphabetically

    def test_a_success_login_standard_user(self):
        # step to open browser
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.maximize_window()
        time.sleep(5)
        # step to fill in email and password
        browser.find_element(By.ID,"user-name").send_keys("standard_user") 
        browser.find_element(By.ID,"password").send_keys("secret_sauce") 
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click()
        time.sleep(5)
        # assert response message
        response_message = browser.find_element(
            By.CLASS_NAME,"inventory_item_name").text
        self.assertEqual(response_message, 'Sauce Labs Backpack')

    def test_b_failed_login_standard_user(self):
        # step to open browser
        browser = self.browser
        browser.get("https://www.saucedemo.com/")
        browser.maximize_window()
        time.sleep(5)
        # step to fill in email and password
        browser.find_element(By.ID,"user-name").send_keys("test") 
        browser.find_element(By.ID,"password").send_keys("test") 
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click()
        time.sleep(5)
        # assert response message
        response_message = browser.find_element(
            By.ID,"login_button_container").text
        self.assertEqual(response_message, 'Epic sadface: Username and password ' 
            +'do not match any user in this service')

if __name__ == "__main__": 
    unittest.main()