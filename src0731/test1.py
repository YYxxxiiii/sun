# Generated by Selenium IDE
import unittest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test073101(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_073101(self):
        self.driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")
        self.driver.set_window_size(550, 692)
        self.driver.find_element(By.ID, "head").click()
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("二十不惑")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        time.sleep(8)

    if __name__ == "__name__":
        unittest.main()
