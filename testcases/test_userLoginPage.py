# -*- coding: utf-8 -*-

import pytest
from pages.UserLoginPage import UserLoginPage


class TestUserLoginPase():

    @pytest.fixture(autouse=True)
    def open_register(self, userLoginPage: UserLoginPage):
        userLoginPage.open("/users/login/")

    def test_user_login_1(self, userLoginPage: UserLoginPage):
        """登录-输入用户名为空，任意密码123456,点登陆按钮，提示：这个字段是必须的"""
        userLoginPage.input_login_username("")
        userLoginPage.input_login_password("123456")
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.error_tips_text() == "这个字段是必须的"

    def test_user_login_2(self, userLoginPage: UserLoginPage):
        """登录-输入邮箱格式不正确“123abc” ,密码123456,点登陆按钮，提示:用户名或密码错误"""
        userLoginPage.input_login_username("123abc")
        userLoginPage.input_login_password("123456")
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.error_tips_text() == "用户名或密码错误"

    def test_user_login_3(self, userLoginPage: UserLoginPage):
        """登录-邮箱格式正确123@qq.com，密码不对:111111，提示：用户名或密码错误 """
        userLoginPage.input_login_username("123@qq.com")
        userLoginPage.input_login_password("111111")
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.error_tips_text() == "用户名或密码错误"

    def test_user_login_4(self, userLoginPage: UserLoginPage, base_url):
        """登录-输入正确的邮箱1234@qq.com，正确的密码:123456，登录成功"""
        userLoginPage.input_login_username("123456@qq.com")
        userLoginPage.input_login_password("123456")
        userLoginPage.click_login_btn()
        # 断言
        assert userLoginPage.error_tips_text() == ""
        url = userLoginPage.driver.current_url
        print("登录后跳转的页面地址:", url)
        assert url == base_url + "/"

    def test_user_forgetPwd_5(self, userLoginPage: UserLoginPage, base_url):
        """登录-忘记密码"""
        userLoginPage.click_forgetPwd_btn()
        # 断言
        url = userLoginPage.driver.current_url
        print("点击忘记密码后跳转的页面地址:", url)
        assert url == base_url + "/users/forgetpwd/"
