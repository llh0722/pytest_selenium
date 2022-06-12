# -*- coding: utf-8 -*-
from common.base import Base


class UserFeedbackIframePage(Base):
    """意见反馈页面"""
    iframe_loc = ("name", 'iframe')
    subject_loc = ("class name", "select1")
    message_loc = ("name", "message")
    email_loc = ("xpath", '//*[@class="form-report"]/label[3]/input')
    send_loc = ("class name", "button")

    def to_iframe(self):
        """切换到iframe页面"""
        self.switch_iframe(self.iframe_loc)

    def select_subject(self, value=""):
        """选中下拉选项"""
        self.select_by_value(self.subject_loc, value)

    def all_options(self):
        """获取所有的选项"""
        all_options = self.select_object(self.subject_loc).options
        all_text = [i.text for i in all_options]
        return all_text

    def selected_subject(self):
        """获取被选中的选项"""
        selected = self.select_object(self.subject_loc).first_selected_option
        return selected.text

    def input_textarea(self, text=""):
        """输入反馈内容"""
        self.send(self.message_loc, text)

    def input_email(self, text=""):
        """输入联系方式"""
        self.send(self.email_loc, text)

    def send_click(self):
        """点send按钮"""
        self.click(self.send_loc)

