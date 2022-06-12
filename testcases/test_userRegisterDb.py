# -*- coding: utf-8 -*-
import pytest

from pages.UserRegisterPage import UserRegisterPage


class TestUserRegisterPage():

    @pytest.fixture()
    def delete_user(self, db):
        sql = 'delete from users_userprofile where username = "123456@qq.com";'
        db.execute(sql)

    @pytest.fixture(autouse=True)
    def open_register(self, userRegisterPage: UserRegisterPage):
        userRegisterPage.open("/users/register/")

    def test_user_register_1(self, userRegisterPage: UserRegisterPage, delete_user):
        userRegisterPage.input_register_email("123456@qq.com")
        userRegisterPage.input_register_password("123456")
        userRegisterPage.click_register_btn()
        # 注册成功断言
        register_result = userRegisterPage.register_success_text()
        print("注册实际结果：", register_result)
        assert register_result == "尊敬的用户，您好，账户已激活成功！"

















