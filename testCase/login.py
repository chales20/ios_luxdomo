#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 上午11:42
# @Author  : Chenzd
# @Site    : 登录测试用例
# @File    : login.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.loginPage import LoginPage
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('-----登录测试开始----')
        cls.driver = MyDriver.cur_driver()

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login()

    @classmethod
    def tearDownClass(cls):
        print('----登录测试结束-----')