# -*- coding: utf-8 -*-
from common.base import Base


class UserInfoPage(Base):
    nick_name_loc = ("id", "nick_name")
    date_day_loc = ("id", "date_day")
    birth_day_loc = ("id", "birth_day")
    # 性别
    # 兴趣
    address_loc = ("id", "address")
    mobile_loc = ("id", "mobile")
    # 邮箱
    click_btn_loc = ("id", "jsEditUserBtn")
    dialog_loc = ("id", ".cont>h2")
    error_tips_loc = ("class name", "error-tips")

    def clear_nick_name(self):
        self.clear(self.nick_name_loc)

    def input_nick_name(self, name=""):
        self.send(self.nick_name_loc, name)

    def click_btn(self):
        self.click(self.click_btn_loc)

    def error_tips(self):
        return self.get_text(self.error_tips_loc)

