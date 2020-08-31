import pytest, os, sys, allure
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.login_page import LoginPage
from base.base_yml import dict_yml_file

def yml_key(key):
    return dict_yml_file("login", key)

class TestLogin():

    def setup(self):
        self.driver = init_driver()
        self.LoginPage = LoginPage(self.driver)

    @allure.step(title="测试登录")
    @pytest.mark.parametrize("dict", yml_key("test_login"))
    def test_login(self, dict):
        username = dict["username"]
        password = dict["password"]
        toast = dict["toast"]
        screen_name = dict["screen"]

        # 输入账号
        allure.attach(username, "输入的用户名")
        self.LoginPage.input_username(username)
        # 输入密码
        allure.attach(password, "输入的密码")
        self.LoginPage.input_password(password)
        # 点击登录
        allure.attach("", "点击登录")
        self.LoginPage.click_login2()

        # 通过toast框提示判定是否登录成功
        allure.attach(toast, "判定登录成功或者失败")
        res = self.LoginPage.is_toast_exist(toast, True, screen_name)
        allure.attach(open('./screen/' + screen_name + '.png', 'rb').read(), '现象截图', allure.attachment_type.PNG)
        assert res


