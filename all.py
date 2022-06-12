# -*- coding: utf-8 -*-
import os

import pytest


if __name__ == '__main__':
    pytest.main()
    """
    allure generate 命令，固定的
    ./temp 临时的json格式报告路径
    -o 输出output
    ./report 生成allure报告的路径
    --clean 清空./report路径下原来的报告
    """
    os.system('allure generate ./temp -o ./report --clean')
    """
    运行所有模块
    pytest_demo.main()
    """

    """
    指定模块运行
    pytest_demo.main(["-vs", "test_case_01.py"])
    """

    """
    # 指定目录运行
    pytest.main(["-vs", "user"])
    """

    """
    通过nodeid指定运行用例
    pytest.main(["-vs", "user/test_case_02.py::TestLogin1::test_05_login"])
    """

    """
    分布式运行
    pytest.main(["-vs", "user", "-n=2"])
    """