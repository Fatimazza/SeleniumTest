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

    def test_b_failed_login_wrong_credentials(self):
        # step to open browser
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(5)
        # step to fill in email and password
        browser.find_element(By.NAME,"username").send_keys("wrong") 
        browser.find_element(By.NAME,"password").send_keys("wrong") 
        browser.find_element(By.XPATH,"//div[@id='app']/div[@class='orangehrm-login-layout']"
            +"/div[@class='orangehrm-login-layout-blob']"
            +"//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(5)
        # assert response message
        response_message = browser.find_element(
            By.CSS_SELECTOR,'p.oxd-alert-content-text').text
        self.assertEqual(response_message, 'Invalid credentials')

    def test_c_failed_login_empty_field(self):
        # step to open browser
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")
        browser.maximize_window()
        time.sleep(5)
        # step to click button without fill in email and password
        browser.find_element(
            By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']" +
            "/div[@class='orangehrm-login-layout-blob']" +
            "//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']"
        ).click()
        time.sleep(5)
        # assert response message
        username_warning_xpath = "//div[@id='app']/div[@class='orangehrm-login-layout']//form[@action='/web/index.php/auth/validate']/div[1]/div/span[.='Required']"
        pass_warning_xpath = "//div[@id='app']/div[@class='orangehrm-login-layout']//form[@action='/web/index.php/auth/validate']/div[2]/div/span[.='Required']"
        err_message_username = browser.find_element(
            By.XPATH, username_warning_xpath).text
        err_message_password = browser.find_element(
            By.XPATH, pass_warning_xpath).text
        self.assertEqual(err_message_username, 'Required')
        self.assertEqual(err_message_password, 'Required')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()