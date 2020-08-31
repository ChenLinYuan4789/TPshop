from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'S003380000161'
# app信息
desired_caps['appPackage'] = 'com.gree.applicationmarket'
desired_caps['appActivity'] = '.mvp.ui.activity.MainActivity'
# 获取toast
desired_caps['automationName'] = 'Uiautomator2'
# 输入中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# 不重置应用
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def find_toast(message):
    ele = driver.find_element(By.XPATH, "//*[contains(@text, '" + message + "')]")
    return ele.text
sleep(1)
driver.press_keycode(4)
print(find_toast("退出"))
sleep(1)

driver.press_keycode(4)
print(find_toast("退出"))
driver.close_app()







