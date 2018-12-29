from base.base_aciton import BaseAciton
import page
"""
负责 设置页面的逻辑
"""
class SettingPage(BaseAciton):
    def __init__(self, driver):
        BaseAciton.__init__(self, driver)

    # 退出当前登录的账号
    def logout_account(self):
        # 1.滑动到页面底端才能看到退出按钮
        self.swipe_screen(1)
        # 2.点击退出按钮
        self.click_element(page.setting_center_login_out_btn)
        # 3.点击弹出对话框的 确定按钮
        self.click_element(page.setting_center_login_dialog_confirm_btn)