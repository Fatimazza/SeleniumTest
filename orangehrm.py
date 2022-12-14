import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #each function begin with "test" and run alphabetically
    def test_a_success_login(self):
        # step to open browser
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(5)
        # step to fill in email and password
        browser.find_element(By.NAME,"username").send_keys("Admin") 
        browser.find_element(By.NAME,"password").send_keys("admin123") 
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']"
            +"/div[@class='orangehrm-login-layout-blob']"
            +"//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(5)
        # assert response message
        response_message = browser.find_element(
            By.XPATH,"//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']"
            +"//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']").text
        self.assertEqual(response_message, 'Admin')

if __name__ == "__main__": 
    unittest.main()