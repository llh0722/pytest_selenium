# -*- coding: utf-8 -*-
import pytest

from pages.UserRegisterPage import UserRegisterPage


class TestUserRegisterPage():

    @pytest.fixture(autouse=True)
    def open_register(self, userRegisterPage: UserRegisterPage):
        userRegisterPage.open("/users/register/")

    def test_user_register_1(self, userRegisterPage: UserRegisterPage):
        """ 注册-输入邮箱为空，密码为空，
        点提交按钮，邮箱/密码输入框红色提示 (class属性包含errorput)"""
        userRegisterPage.input_register_email("")
        userRegisterPage.input_register_password("")
        userRegisterPage.click_register_btn()
        # 邮箱输入框断言
        email_result = userRegisterPage.get_email_attribute()
        print("邮箱输入框实际结果：", email_result)
        assert "errorput" in email_result
        # 密码输入框断言
        password_result = userRegisterPage.get_password_attribute()
        print("密码输入框实际结果：", password_result)
        assert "errorput" in password_result

    def test_user_register_2(self, userRegisterPage: UserRegisterPage):
        """ 注册-邮箱格式不正确，密码为空，
        点提交按钮，邮箱输入框红色提示(class 属性包含errorput)"""
        userRegisterPage.input_register_email("123456")
        userRegisterPage.input_register_password("")
        userRegisterPage.click_register_btn()
        # 邮箱输入框断言
        email_result = userRegisterPage.get_email_attribute()
        print("邮箱输入框实际结果：", email_result)
        assert "errorput" in email_result

    def test_user_register_3(self, userRegisterPage: UserRegisterPage):
        """
        注册-邮箱格式正确(111@qq.com),密码为空，
        点提交按钮，密码框提示红色（class属性errorput）
        """
        userRegisterPage.input_register_email("123456@qq.com")
        userRegisterPage.input_register_password("")
        userRegisterPage.click_register_btn()
        # 密码输入框断言
        password_result = userRegisterPage.get_password_attribute()
        print("密码输入框实际结果：", password_result)
        assert "errorput" in password_result

    def test_user_register_4(self, userRegisterPage: UserRegisterPage):
        """
        注册-邮箱格式正确(111@qq.com), 密码小于6位，
        点提交按钮，密码框提示红色（class属性errorput）
        """
        userRegisterPage.input_register_email("123456@qq.com")
        userRegisterPage.input_register_password("12345")
        userRegisterPage.click_register_btn()
        # 密码输入框断言
        password_result = userRegisterPage.get_password_attribute()
        print("密码输入框实际结果：", password_result)
        assert "errorput" in password_result

    def test_user_register_5(self, userRegisterPage: UserRegisterPage):
        """
        注册-邮箱格式正确(111@qq.com), 密码大于20位，
        点提交按钮，密码框提示红色（class属性errorput）
        """
        userRegisterPage.input_register_email("123456@qq.com")
        userRegisterPage.input_register_password("012345678909876543210")
        userRegisterPage.click_register_btn()
        # 密码输入框断言
        password_result = userRegisterPage.get_password_attribute()
        print("密码输入框实际结果：", password_result)
        assert "errorput" in password_result

    def test_user_register_6(self, userRegisterPage: UserRegisterPage):
        """注册-邮箱输入框，输入文本：111@qq.com，再清空文本，输入框为空"""
        userRegisterPage.input_register_email("123456@qq.com")
        assert userRegisterPage.get_email_attr(attr="value") == "123456@qq.com"
        # 清空文本断言
        userRegisterPage.clear_email()
        assert userRegisterPage.get_email_attr(attr="value") == ""

    def test_user_register_7(self, userRegisterPage: UserRegisterPage):
        """'注册-密码框输入文本：123456，显示******'"""
        userRegisterPage.input_register_password("012345")
        assert userRegisterPage.get_password_attr(attr="value") == "012345"
        # 判断显示******'"""
        print(userRegisterPage.get_password_attr(attr="type"))
        assert userRegisterPage.get_password_attr(attr="type") == "password"
        # 清空文本断言
        userRegisterPage.clear_password()
        assert userRegisterPage.get_password_attr(attr="value") == ""

    def test_user_register_8(self, userRegisterPage: UserRegisterPage, base_url):
        """注册-点页面“回到首页”按钮，点击跳转到首页/"""
        link = userRegisterPage.get_href_link('//*[@class="index-font"]')
        print("点击回到首页后的地址：", link)
        assert link == base_url+"/"

    def test_user_register_9(self, userRegisterPage: UserRegisterPage, base_url):
        """注册-点页面“logo图片”，点击跳转到首页/"""
        link = userRegisterPage.get_href_link('//*[@class="index-logo"]')
        print("点击logo图片回到首页后的地址：", link)
        assert link == base_url+"/"

    def test_user_register_10(self, userRegisterPage: UserRegisterPage, base_url):
        """注册-点页面“登陆”按钮，点击跳转到登陆页/users/login/"""
        link = userRegisterPage.get_href_link('//*[@class="fr hd-bar"]/li[2]/a[1]')
        print("点击登录按钮回到登录后的地址：", link)
        assert link == base_url + "/users/login/"

    def test_user_register_11(self, userRegisterPage: UserRegisterPage, base_url):
        """注册-点页面“注册”按钮，点击跳转到登陆页/users/register/"""
        link = userRegisterPage.get_href_link('//*[@class="active"]/a')
        print("点击注册按钮回到注册页后的地址：", link)
        assert link == base_url + "/users/register/"

    def test_user_register_12(self, userRegisterPage: UserRegisterPage, base_url):
        """注册-点页面“立即登陆”按钮，点击跳转到登陆页/users/login/"""
        link = userRegisterPage.get_href_link('//*[@class="form-p"]/a[1]')
        print("点击立即登录按钮回到登录页后的地址：", link)
        assert link == base_url + "/users/login/"
