import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        # step to open browser
        browser = self.browser
        browser.get("https://opensource-demo.orangehrmlive.com")

if __name__ == "__main__": 
    unittest.main()