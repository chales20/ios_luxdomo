#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 上午10:07
# @Author  : Chenzd
# @Site    : 
# @File    : inputPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
class InputPage(BasePage):

    # 推送按钮开关
    TypeSwitch = "type=='XCUIElementTypeSwitch' and visible=true"
    # 首页其它设备里面的传感器名称
    StaticText = "type=='XCUIElementTypeStaticText'"
    roomNameEdit = "type=='XCUIElementTypeTextField'"

    # ------------------推送按钮--------------
    def pushSwitch_state(self):
        ele = self.findIpt(self.TypeSwitch)
        suc = 0
        if ele:
            res = self.element_attribute(ele, 'visible')
            while res == 'false':
                self.swipe_up()
                ele = self.findIpt(self.TypeSwitch)
                res = self.element_attribute(ele, 'visible')
            text = self.element_attribute(ele, 'value')
            if text == '1':  # 选中的值为1
                print('结果：按钮默认开启')
            else:
                print('结果：按钮默认关闭')
        else:
            suc = 1
            print('结果：无推送按钮')
        return suc

    def pushSwitch_control(self):
        ele = self.findIpt(self.TypeSwitch)
        text1 = self.element_attribute(ele, 'value')
        self.click_element(ele)
        text2 = self.element_attribute(ele, 'value')
        suc = 0
        if text1 != text2:
            print('结果：按钮控制成功')
        else:
            suc = 1
            print('结果：按钮控制失败')
        print('再控一次，按钮回到初始状态')
        self.click_element(ele)
        return suc

    def random_enter_one(self):
        eles = self.findIpts(self.StaticText)
        ran = random.randint(1, len(eles)-1)
        text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('选择【%s】' % text)
        return text

    def is_ele(self, name):
        ele = self.wait_for_element(id=name)
        self.click_element(ele)
        ele2 = self.findIpt(self.roomNameEdit)
        suc = 0
        if not ele2:
            print('结果：长按正常，其它设备不能进入名称编辑/移动等')
        else:
            suc = 1
            print('结果：长按异常')
        return suc
