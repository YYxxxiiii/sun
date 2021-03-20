from selenium import webdriver#引入网页驱动
driver = webdriver.Firefox()#使用网页驱动来运行火狐浏览器
driver.get('https://blog.csdn.net/qq_37245397')#通过驱动来执行指定的网页