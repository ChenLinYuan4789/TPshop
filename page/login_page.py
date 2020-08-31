from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class LoginPage(BaseAction):

    main_button = By.XPATH, ["text,未登录,1", "resource-id,com.ss.android.article.news:id/dfk"]
    login_button = By.XPATH, "text,登录,1"
    login_way_button = By.XPATH, "text,密码登录,1"
    username_view = By.XPATH, "text,手机号/邮箱,1"
    password_view = By.XPATH, "text,密码,1"
    login_button2 = By.ID, "com.ss.android.article.news:id/qu"
    user_text = By.ID, "com.ss.android.article.news:id/b91"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        # 点击我的
        self.click_main()
        # 点击登录/注册
        self.click_login()
        # 选择密码登录
        self.click_login_way()

    def click_main(self):
        self.click(self.main_button)

    def click_login(self):
        self.click(self.login_button)

    def click_login_way(self):
        self.click(self.login_way_button)

    def input_username(self, text):
        self.send_keys(self.username_view, text)

    def input_password(self, text):
        self.send_keys(self.password_view, text)

    def click_login2(self):
        self.click(self.login_button2)









