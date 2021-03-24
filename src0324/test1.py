import unittest
from selenium import webdriver
import time

class test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://home.firefoxchina.cn/")

        self.driver.maximize_window()
        time.sleep(3)
    def tearDown(self):
        self.driver.quit()

    @unittest.skip("skipping")
    def test_ck(self):
        self.driver.find_element_by_id("search-key").send_keys("justinbieber")
        self.driver.find_element_by_id("search-submit").click()
        time.sleep(8)

    def test_d(self):
        self.driver.find_element_by_id("search-key").send_keys("乃万")
        self.driver.find_element_by_id("search-submit").click()
        self.driver.implicitly_wait(8)
        self.driver.find_element_by_link_text(u"乃万-百度百科").click()
        time.sleep(8)


if __name__ == '__main__':
    unittest.main()
