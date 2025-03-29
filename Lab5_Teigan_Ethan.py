#Names: Teigan Pritchard, Ethan Smallwood
#Date: 2025/03/28
#Filename: Lab5_Teigan_Ethan.py
#Description: using selenium to test e-commerce website

# Importing libraries
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MagentoTest(unittest.TestCase):

 @classmethod
 def setUpClass(cls):
     cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
     cls.driver.maximize_window()
     cls.driver.get("https://magento.softwaretestingboard.com/")

 @classmethod
 def tearDownClass(cls):
     cls.driver.quit()
 def hover_element(self, element):
     """Performs a hover action on the given element."""
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()

 def scroll_into_view(self, element):
     """Scrolls the element into view to ensure it's interactable."""
     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

 def test_01_navigate_to_product_page(self):
     """Navigate to Women -> Tops -> Hoodies & Sweatshirts"""
     print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
     driver = self.driver

    #navigates into womens hoodies / sweatshirts
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Women"))).click()
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tops"))).click()
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))).click()
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hoodies & Sweatshirts')]"))).click()

 def test_02_apply_filters(self):
     """Apply Filters"""
     print("Applying filters: Pullover, Size: M, Color: Purple")
     driver = self.driver
     #opens style and selects pullover filter
     style = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Style']")))
     style.click()
     pullover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='layered-filter-block']//div[1]//div[2]//ol[1]//li[3]//a[1]")))
     pullover.click()

    #opens size and selects medium filter
     size = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Size']")))
     size.click()
     m = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='M']//div[contains(@class,'swatch-option text')][normalize-space()='M']")))
     m.click()

    #opens price and selects $50-$59 filter
     price = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Price']")))
     price.click()
     money = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='$59.99']")))
     money.click()

    #opens colour and selects purple filter
     colour = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Color']")))
     colour.click()
     purple = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Purple']//div[contains(@class,'swatch-option color')]")))
     purple.click()

    #opens material and selects polyester filter
     material = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Material']")))
     material.click()
     polyester = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[4]//div[2]//ol[1]//li[3]//a[1]")))
     polyester.click()

 def test_03_add_to_cart(self):
     """Select Product and Add to Cart"""
     print("Selecting a product and adding it to the cart")
     driver = self.driver
     time.sleep(2)
     #adds atumn pullie to cart
     product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Autumn Pullie-M-Purple']")))
     self.hover_element(product)
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Add to Cart']"))).click()

 def test_04_checkout(self):
     """View Cart and Proceed to Checkout"""
     print("Proceeding to checkout")
     driver = self.driver
     time.sleep(2)
    #clicks view cart then proceeds to checkout
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='action showcart']"))).click()
     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='top-cart-btn-checkout']"))).click()

 def test_05_validate_order_summary(self):
     """Validate Order Summary"""
     print("Validating the order summary")
     driver = self.driver
     #opens summary and checks that autumn puillie is the top added to cart
     summary = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='title']")))
     summary.click()
     actual_text = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//strong[@class='product-item-name']")))
     assert "Autumn Pullie" in actual_text.text, "Order Summary does not contain the selected product"


if __name__ == "__main__":
 suite = unittest.TestSuite()
 #runs all test cases
 suite.addTest(MagentoTest("test_01_navigate_to_product_page"))
 suite.addTest(MagentoTest("test_02_apply_filters"))
 suite.addTest(MagentoTest("test_03_add_to_cart"))
 suite.addTest(MagentoTest("test_04_checkout"))
 suite.addTest(MagentoTest("test_05_validate_order_summary"))

 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(suite)


