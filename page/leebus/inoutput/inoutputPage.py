#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 下午1:24
# @Author  : Chenzd
# @Site    : 
# @File    : inoutputPage.py
# @Software: PyCharm
# @company:  LEELEN
import random

from page.basePage import BasePage
class InoutputPage(BasePage):

    StaticText = "type=='XCUIElementTypeStaticText'"
    # 选择开关类型
    TypeButton = "type=='XCUIElementTypeButton'"
    def switchType(self):
        eles = self.findIpts(self.StaticText)
        text1 = self.getText_element(eles[5])
        print('开关类型为【%s】' % text1)
        self.click_element(eles[5])
        eles_list = self.findIpts(self.TypeButton)
        ran = random.randint(2,4)
        text_change = self.element_attribute(eles_list[ran], 'name')
        print('更改类型为【%s】' % text_change)
        self.click_element(eles_list[ran])
        eles = self.findIpts(self.StaticText)
        text2 = self.getText_element(eles[5])
        print('获取更改后的开关类型【%s】' % text2)
        suc = 0
        if text_change == '取消':
            if text1 == text2:
                print('结果：更改功能正常')
            else:
                suc = 1
                print('结果：更改功能异常')
        else:
            if text_change == text2:
                print('结果：更改功能正常')
            else:
                suc = 1
                print('结果：更改功能异常')
        return suc

    def is_pushSwitch(self, ele):
        ele = self.findIpt(ele)
        suc = 0
        print('判断是否有推送按钮开关')
        if not ele:
            suc = 1
            print('结果：无，跳过推送按钮推送')
        else:
            print('结果：有，进行推送按钮操作')
        return suc
