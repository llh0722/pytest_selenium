# -*- coding: utf-8 -*-
import time
import allure
import pytest

from pages.UserFeedbackIframePage import UserFeedbackIframePage


class TestUserFeedbackIframePage():

    @pytest.fixture(autouse=True)
    def open_feedback(self, userFeedbackIframePage: UserFeedbackIframePage):
        userFeedbackIframePage.open("/users/feedbackiframe/")
        # 切换到iframe
        userFeedbackIframePage.to_iframe()

    @allure.title("意见反馈 - 反馈类型有三个下拉选项：改进建议，页面布局，提BUG")
    def test_feedback_1(self, userFeedbackIframePage: UserFeedbackIframePage):
        """意见反馈 - 反馈类型有三个下拉选项：改进建议，页面布局，提BUG"""
        all_options = userFeedbackIframePage.all_options()
        print("所有的下拉选项内容：", all_options)
        assert all_options == ['改进建议', '页面布局', '提BUG']

    def test_feedback_2(self, userFeedbackIframePage: UserFeedbackIframePage):
        """意见反馈-反馈类型选页面布局，被选中：页面布局"""
        userFeedbackIframePage.select_subject(value="页面布局")
        assert userFeedbackIframePage.selected_subject() == "页面布局"
        time.sleep(3)
        """意见反馈-反馈类型选页面布局，被选中：提BUG"""
        userFeedbackIframePage.select_subject(value="提BUG")
        assert userFeedbackIframePage.selected_subject() == "提BUG"
        time.sleep(3)
        """意见反馈-反馈类型选页面布局，被选中：改进建议"""
        userFeedbackIframePage.select_subject(value="改进建议")
        assert userFeedbackIframePage.selected_subject() == "改进建议"
        time.sleep(3)

    @pytest.mark.parametrize("test_input", ["页面布局", "提BUG", "改进建议"])
    def test_feedback_3(self, userFeedbackIframePage: UserFeedbackIframePage, test_input):
        """意见反馈-反馈类型选页面布局，被选中：页面布局"""
        userFeedbackIframePage.select_subject(value=test_input)
        assert userFeedbackIframePage.selected_subject() == test_input
        time.sleep(3)

    def test_feedback_4(self, userFeedbackIframePage: UserFeedbackIframePage):
        """'意见反馈，反馈类型：改进建议，反馈内容为空，联系方式为空，
        点send提交按钮，alert弹窗提示：提交成功！"""
        userFeedbackIframePage.select_subject(value="提BUG")
        userFeedbackIframePage.input_textarea("dfdfdsfs")
        userFeedbackIframePage.input_email("asdadadas")
        userFeedbackIframePage.send_click()
        alert_text = userFeedbackIframePage.get_alert_text()
        assert alert_text == "提交成功！"

    @pytest.mark.parametrize("test_input, expected", [
        [{"subject": "改进建议", "textarea": "", "email": ""}, "提交成功！"],
        [{"subject": "改进建议", "textarea": "测试内容test", "email": ""}, "提交成功！"],
        [{"subject": "改进建议", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "改进建议", "textarea": "测试内容test", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "页面布局", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
        [{"subject": "提BUG", "textarea": "", "email": "1111@qq.com"}, "提交成功！"],
    ])
    def test_feedback_5(self, userFeedbackIframePage: UserFeedbackIframePage, test_input, expected):
        """"""
        userFeedbackIframePage.select_subject(value=test_input["subject"])
        userFeedbackIframePage.input_textarea(test_input["textarea"])
        userFeedbackIframePage.input_email(test_input["email"])
        userFeedbackIframePage.send_click()
        alert_text = userFeedbackIframePage.get_alert_text()
        assert alert_text == expected
