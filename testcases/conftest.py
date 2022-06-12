# -*- coding: utf-8 -*-
import os.path

import allure
import pytest
from selenium import webdriver

from common.connect_mysql import dbinfo, DbConnect
from pages.UserFeedbackIframePage import UserFeedbackIframePage
from pages.UserInfoPage import UserInfoPage
from pages.UserLoginPage import UserLoginPage
from pages.UserRegisterPage import UserRegisterPage


_driver = None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例的状态的钩子函数
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况，不包含setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = "(%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(_driver, "get_screenshot_as_png"):
            with allure.step("添加失败截图..."):
                allure.attach(_driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope="session", name="driver")
def browser():
    global _driver
    if _driver is None:
        _driver = webdriver.Chrome()
    _driver.maximize_window()
    yield _driver
    _driver.quit()

# @pytest.fixture(scope="session", name="driver")
# def browser():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="session")
def base_url():
    url = 'http://49.235.92.12:8200'
    return url


@pytest.fixture(scope="session")
def userRegisterPage(driver, base_url):
    user_register = UserRegisterPage(driver, base_url)
    return user_register


@pytest.fixture(scope="session")
def userLoginPage(driver, base_url):
    user_login = UserLoginPage(driver, base_url)
    return user_login


@pytest.fixture(scope="session")
def userFeedbackIframePage(driver, base_url):
    user_feedback = UserFeedbackIframePage(driver, base_url)
    return user_feedback


@pytest.fixture(scope="session")
def db():
    _db = DbConnect(dbinfo, "online")
    yield _db
    _db.close()


@pytest.fixture(scope="session")
def login_driver(driver, userLoginPage: UserLoginPage):
    userLoginPage.open("/users/login/")
    userLoginPage.input_login_username("123456@qq.com")
    userLoginPage.input_login_password("123456")
    userLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope="session")
def userInfoPage(login_driver, base_url):
    user_info = UserInfoPage(login_driver, base_url)
    return user_info
