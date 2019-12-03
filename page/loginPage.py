#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 下午1:56
# @Author  : Chenzd
# @Site    : 
# @File    : loginPage.py
# @Software: PyCharm
# @company:  LEELEN
from page.basePage import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):

    name = (By.XPATH, "//*[@type='XCUIElementTypeTextField']")
    passwd = (By.XPATH,"//*[@type='XCUIElementTypeSecureTextField']")
    # loginBtn = BasePage().wait_for_element(id='登录')

    def login(self):
        self.input(self.name, '15606920337')
        self.input(self.passwd, '123456')
        loginBtn = self.wait_for_element(id='登录')
        self.click_element(loginBtn)