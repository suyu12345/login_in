from base.base_aciton import BaseAciton
import page
"""
负责 个人页面逻辑
"""
class PersonCenterPage(BaseAciton):
    def __init__(self, driver):
        BaseAciton.__init__(self, driver)

       # 点击个人中心的设置按钮
    def click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)


    def is_login_success(self):
        try:
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False