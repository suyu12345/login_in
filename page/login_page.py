import allure

from base.base_aciton import BaseAciton
import page
"""
负责登录页面的逻辑
"""
class LoginPage(BaseAciton):
    def __init__(self, driver):
        BaseAciton.__init__(self, driver)


      # 点击登录逻辑
    def login_in(self, name, pwd):
        # 输入账号    账号的数据不能写死,应该从脚本里动态的传入
        self.input_element_content(page.login_username_id, name)
        # 输入密码
        self.input_element_content(page.login_password_id, pwd)
        # 点击登录按钮
        self.click_element(page.login_login_in_btn)

      #关闭登录页面的逻辑
    def close_login_page(self):
        self.click_element(page.login_login_out_btn)
