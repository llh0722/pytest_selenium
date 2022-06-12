# -*- coding: utf-8 -*-
import pytest
from pages.UserInfoPage import UserInfoPage


class TestUserInfoPage():

    @pytest.fixture(autouse=True)
    def open_userInfo(self, userInfoPage:UserInfoPage):
        userInfoPage.open("/users/userinfo/")

    def test_userInfo_1(self, userInfoPage: UserInfoPage):
        userInfoPage.clear_nick_name()
        userInfoPage.input_nick_name("")
        userInfoPage.click_btn()
        text = userInfoPage.error_tips()
        print(text)
        assert text == "请输入昵称！"
