"""
首页
"""

from selenium.webdriver.common.by import By
# 1.点击我的按钮
home_my_button = By.ID,'com.yunmall.lc:id/tab_me'
"""
注册页面
"""
#  1.点击注册已存在的账号
# sign_in_exit_account_id = By.ID,'com.yunmall.lc:id/textView1'
sign_in_exit_account_id = By.ID, "com.yunmall.lc:id/gotologon"
"""
登录页面
"""
# 1.定位登录账号
login_username_id = By.ID,"com.yunmall.lc:id/logon_account_textview"
# 2.定位登录密码
login_password_id = By.ID,"com.yunmall.lc:id/logon_password_textview"
# 3.点击登录按钮
login_login_in_btn = By.ID,"com.yunmall.lc:id/logon_button"
# 4. 退出登录
login_login_out_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
"""
个人中心页面
"""
# 1.点击个人中心的设置按钮
# 2. 定位到我的订单
person_center_setting_btn = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
person_center_all_order = By.ID,"com.yunmall.lc:id/order_more_txt"

"""
设置中心
"""
setting_center_login_out_btn =By.ID,"com.yunmall.lc:id/setting_logout"
setting_center_login_dialog_confirm_btn =By.ID,"com.yunmall.lc:id/ymdialog_right_button"
