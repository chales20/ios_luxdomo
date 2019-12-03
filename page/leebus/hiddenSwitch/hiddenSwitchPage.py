#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 上午9:53
# @Author  : Chenzd
# @Site    : 隐藏式页面类
# @File    : hiddenSwitchPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
from page.basePage import BasePage

class HiddenSwitchPage(BasePage):

    # 选择开关类型的按钮
    TypeButton = "type=='XCUIElementTypeButton'"

    StaticText = "type=='XCUIElementTypeStaticText'"

    def switchType(self):
        eles = self.findIpts(self.StaticText)
        self.click_element(eles[5])
        eles_btn = self.findIpts(self.TypeButton)
        eles_list = [eles_btn[2], eles_btn[3]]
        ran = random.randint(0, len(eles_list)-1)
        text = self.getText_element(eles_list[ran])
        print('随机选择开关类型【%s】' % text)
        self.click_element(eles_list[ran])
        eles = self.findIpts(self.StaticText)
        text2 = self.getText_element(eles[5])
        suc = 0
        if text == text2:
            print('结果：开关类型正常')
        else:
            suc = 1
            print('结果：开关类型异常')
        return suc
