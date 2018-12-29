from base.base_aciton import BaseAciton
import page

"""
负责 首页 分类 购物车  我的 业务
"""
class HomePage(BaseAciton):
    # 初始化函数  动态把driver传入
    def __init__(self, driver):
        BaseAciton.__init__(self, driver)

    # 点击首页 我的 按钮
    def click_my_button(self):
        self.click_element(page.home_my_button)
        