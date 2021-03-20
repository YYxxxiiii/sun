import time
import os

from selenium import webdriver

driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath("F:/360MoveData/Users/Dell/Desktop/selenium2html/alert.html")
driver.get(file_path)
time.sleep(3)
driver.maximize_window()
# 定位点击按钮
driver.find_element_by_id("tooltip").click()
time.sleep(10)

# 得到操作alert弹出框的句柄
alert = driver.switch_to.alert

# 弹出输出框内容
text = alert.text
print("text = " + text)
time.sleep(5)
alert.accept()


time.sleep(6)
driver.quit()