import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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
        self.assertIn('Username and password do not match any user in this service', response_message)

    def test_c_success_open_product_detail(self):
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
        product_3_xpath = "/html//div[@id='inventory_container']/div/div[@id='inventory_container']/div/div[3]/div[@class='inventory_item_description']/div[@class='inventory_item_label']/a[@href='#']/div[@class='inventory_item_name']"
        response_message = browser.find_element(
            By.XPATH,product_3_xpath).text
        self.assertEqual(response_message, 'Sauce Labs Bolt T-Shirt')
        # step to go to detail page
        browser.find_element(By.XPATH,product_3_xpath).click()
        time.sleep(3)
        # assert response message
        product_name = browser.find_element(
            By.CSS_SELECTOR,"div.inventory_details_name").text
        product_desc = browser.find_element(
            By.CSS_SELECTOR,"div.inventory_details_desc").text
        product_price = browser.find_element(
            By.CSS_SELECTOR,"div.inventory_details_price").text
        product_image = browser.find_element(
            By.TAG_NAME,"img").get_attribute("src")
        self.assertEqual(product_name, 'Sauce Labs Bolt T-Shirt')
        self.assertIn('Get your testing superhero on with the Sauce Labs bolt T-shirt', product_desc)
        self.assertEqual(product_price, '$15.99')
        self.assertIn('data:image/png;base64', product_image)

    def test_d_success_add_product_to_cart(self):
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
        product_3_xpath = "/html//div[@id='inventory_container']/div/div[@id='inventory_container']/div/div[3]/div[@class='inventory_item_description']/div[@class='inventory_item_label']/a[@href='#']/div[@class='inventory_item_name']"
        response_message = browser.find_element(
            By.XPATH,product_3_xpath).text
        self.assertEqual(response_message, 'Sauce Labs Bolt T-Shirt')
        # step to add product to cart
        browser.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
        browser.find_element(By.ID,"shopping_cart_container").click()
        time.sleep(3)
        # assert response message
        product_name = browser.find_element(
            By.CSS_SELECTOR,"div.inventory_item_name").text
        product_qty = browser.find_element(
            By.CSS_SELECTOR,"div.cart_quantity").text
        self.assertEqual(product_name, 'Sauce Labs Bolt T-Shirt')
        self.assertEqual(product_qty, '1')

    def test_e_success_logout(self):
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
        # step to logout
        browser.find_element(By.ID,"react-burger-menu-btn").click()
        time.sleep(3)
        browser.find_element(By.LINK_TEXT,"Logout").click()
        time.sleep(5)
        # assert response message
        response_message = browser.find_element(
            By.XPATH,"/html//input[@id='login-button']").get_attribute("value")
        self.assertEquals(response_message, "Login")

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__": 
    # run all test
    unittest.main()
    
    # run specific test
    # unittest.TextTestRunner().run(
    #    TestLogin('test_a_success_login_standard_user'))