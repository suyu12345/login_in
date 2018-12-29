import os,sys
sys.path.append(os.getcwd())
from base.read_data import read_data
import pytest
sys.path.append(os.getcwd())
from page.navigation_page import NavigationPage
from base.base_driver import init_driver
import time


# 获取模拟的yaml数据
def get_data():
    data_list = []
    data = read_data("login_data.yaml")
    # print(data)
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        tag = data2.get("tag")
        except_msg = data2.get("except_msg")
        get_toast_msg = data2.get("get_toast_msg")
        data_list.append((name, passwd, tag, except_msg, get_toast_msg))
    return data_list

class TestLogin:
    #初始化导航类
    def setup_class(self):
        #1.初始化driver对象
        self.driver = init_driver("com.yunmall.lc","com.yunmall.ymctoc.ui.activity.MainActivity")
        #2.初始化导航对象
        self.navigation_page = NavigationPage(self.driver)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()
    #测试登录业务
    @pytest.mark.parametrize('username,password,tag,except_msg, get_toast_msg',get_data())
    def test_login(self,username,password,tag, except_msg, get_toast_msg,):
        # 1.点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        # 2.点击已有账号
        self.navigation_page.get_sign_in_page_obj().click_exit_accout()
        # 3.输入用户名密码 点击登录
        self.navigation_page.get_login_page_obj().login_in(username,password)
        if tag == 1:
            try:
                # 判断是否登陆成功
                login_state = self.navigation_page.get_person_center_page_obj().is_login_success()
            # 点击个人中心的设置按钮
                self.navigation_page.get_person_center_page_obj().click_person_center_setting()
            # 点击退出
                self.navigation_page.get_setting_page_obj().logout_account()
                # 断言如果没有登录成功还是会保存一个截图
                assert login_state, self.navigation_page.get_person_center_page_obj().get_screen()
            except:
                self.navigation_page.get_person_center_page_obj().get_screen()
                # 然后关闭这个软件
                self.navigation_page.get_login_page_obj().close_login_page()

        else:
            try:
                toast_message = self.navigation_page.get_person_center_page_obj().get_toast_message(get_toast_msg)
                # 断言一下 一起结果是否和抓到的吐司结果一致,如果不一致,就会给截图
                assert toast_message == except_msg,self.navigation_page.get_person_center_page_obj().get_screen()
            #      表示最后一定会执行
            finally:
                # 5.关闭当前登录页面
                self.navigation_page.get_login_page_obj().close_login_page()

