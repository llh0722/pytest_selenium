# -*- coding: utf-8 -*-
from common.base import Base


class UserRegisterPage(Base):
    user_email_loc = ("id", "id_email")
    user_password_loc = ("id", "id_password")
    user_registerBtn_loc = ("id", "jsEmailRegBtn")
    back_index_loc = ("class name", "index-font")
    login_link_loc = ("css selector", ".form-p>a")
    emai_class_loc = ("xpath", '//*[@id="id_email"]/..')
    password_class_loc = ("xpath", '//*[@id="id_password"]/..')
    register_success_loc = ("css selector", 'body>h1')

    def input_register_email(self, email=""):
        """输入邮箱"""
        self.send(self.user_email_loc, email)

    def input_register_password(self, password=""):
        """输入密码"""
        self.send(self.user_password_loc, password)

    def click_register_btn(self):
        """点注册按钮"""
        self.click(self.user_registerBtn_loc)

    def register_success_text(self):
        return self.get_text(self.register_success_loc)

    def clear_email(self):
        """清空邮箱输入框"""
        self.clear(self.user_email_loc)

    def clear_password(self):
        """清空密码输入框"""
        self.clear(self.user_password_loc)

    def get_email_attribute(self):
        """获取邮箱输入框class属性"""
        return self.get_attribute(self.emai_class_loc, "class")

    def get_password_attribute(self):
        """获取密码输入框class属性"""
        return self.get_attribute(self.password_class_loc, "class")

    def get_email_attr(self, attr="value"):
        """获取邮箱的属性"""
        return self.get_attribute(self.user_email_loc, attr)

    def get_password_attr(self, attr="type"):
        """获取密码输入框的属性"""
        return self.get_attribute(self.user_password_loc, attr)

    def get_href_link(self, xpath_loc):
        """获取a标签的href属性, xpath定位"""
        href_link_loc = ("xpath", xpath_loc)
        return self.get_attribute(href_link_loc, "href")



