from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '31063b33'
    # app信息
    desired_caps['appPackage'] = 'com.ss.android.article.news'
    desired_caps['appActivity'] = '.activity.MainActivity'
    # 获取toast
    desired_caps['automationName'] = 'Uiautomator2'
    # 输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 不重置应用
    desired_caps['noReset'] = True


    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)