#Names: Teigan Pritchard, Ethan Smallwood
#Program Name: Lab5_Ethan_Teigan.py
#Date: 03/28/2025
#Description: selenium testing code for a e-commerce website

# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pytest
import unittest

class TestLab5(unittest.TestCase):

  def setup_method(self,method):
    # Initialize the WebDriver
    self.driver = webdriver.Chrome()
  
  def teardown_method(self,method):
     self.driver.quit()

  def test_lab5EthanTeigan(self):
    self.driver.get("https://magento.softwaretestingboard.com")
    time.sleep(3)
    

    self.driver.find_element(By.XPATH, "//span[text()='Women']").click()
    self.driver.find_element(By.XPATH, "//span[text()='Tops']").click()
    self.driver.find_element(By.XPATH, "//span[text()='Hoodies & Sweatshirts']").click()

    style_filter = self.driver.find_element(By.XPATH, "//span[text()='Pullover']")
    style_filter.click()


    self.driver.switch_to.frame("frame_name")
    add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart")
    add_to_cart_button.click()
    self.driver.switch_to.default_content()

    cart_icon = self.driver.find_element(By.ID, "cart-icon")
    cart_icon.click()
    checkout_button = self.driver.find_element(By.XPATH, "//button[text()='Proceed to Checkout']")
    checkout_button.click()
  
    order_summary = self.driver.find_element(By.CLASS_NAME, "order-summary")
    assert "Pullover" in order_summary.text, "Order summary does not include the selected item"

    self.driver.quit()