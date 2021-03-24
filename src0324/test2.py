import time

from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://home.firefoxchina.cn/")
browser.maximize_window()
# browser.find_element_by_css_selector("#login_form > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys("abc")
# browser.find_element_by_xpath("//*[@id='login_form']/div[3]/div/input").send_keys("123")
# 
# browser.find_element_by_xpath("//*[@id='login_form']/div[6]/input[2]").submit()
# 
# time.sleep(2)
# div = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]")
# buttons = div.find_elements_by_tag_name("button")
# buttons[0].click()

browser.find_element_by_id("search-key").send_keys("乃万")
browser.find_element_by_id("search-submit").click()
browser.implicitly_wait(10)
title = browser.title
print(title)
# browser.find_element_by_link_text(u"乃万 - 百度百科").click()
time.sleep(8)

time.sleep(10)
browser.quit()