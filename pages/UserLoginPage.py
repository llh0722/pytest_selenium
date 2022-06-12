# -*- coding: utf-8 -*-
from common.base import Base


class UserLoginPage(Base):
    """用户登录页"""
    login_username_loc = ("id", "username")
    login_password_loc = ("id", "password_l")
    login_loginBtn_loc = ("id", "jsLoginBtn")
    login_forgetPwd_loc = ("link text", "忘记密码？")
    # login_forgetPwd_loc = ("css selector", ".auto-box>a")
    error_tips_loc = ("class name", "errorlist")
    tips_loc = ("id", "jsLoginTips")

    def input_login_username(self, user=''):
        """登录用户名"""
        self.send(self.login_username_loc, user)

    def input_login_password(self, password=''):
        """登录密码"""
        self.send(self.login_password_loc, password)

    def click_login_btn(self):
        """点击登录按钮btn"""
        self.click(self.login_loginBtn_loc)

    def error_tips_text(self):
        """登录失败提示语"""
        tips = self.get_text(self.error_tips_loc)
        if not tips:
            tips = self.get_text(self.tips_loc)
        return tips

    def click_forgetPwd_btn(self):
        """点击忘记密码按钮btn"""
        self.click(self.login_forgetPwd_loc)