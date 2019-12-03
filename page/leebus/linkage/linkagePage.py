#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 上午10:49
# @Author  : Chenzd
# @Site    : 
# @File    : linkagePage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.leebus.commonPage import CommonPage
from page.basePage import BasePage
class linkagePage(BasePage):

    TypeButton = "type=='XCUIElementTypeButton'"
    condition = "type=='XCUIElementTypeStaticText' and visible=true"
    bottom_btn = "type=='XCUIElementTypeButton' and name=='btn spe bottom'"

    # 切换到联动选项卡，并确认是否切换成功
    def enter_linkage(self, num):
        time.sleep(2)
        eles = self.findIpts(self.TypeButton)
        self.click_element(eles[num])
        eles = self.findIpts(self.TypeButton)
        res = self.element_attribute(eles[num], 'value')
        suc = 0
        if res == '1':
            print('结果：切换成功')
        else:
            suc = 1
            print('结果：切换失败')
        return suc

    # 点击添加按钮
    def add_linkage(self):
        ele = self.wait_for_element(id='添加')
        self.click_element(ele)



    # 添加联动条件
    def add_condition(self):
        eles = self.findIpts(self.condition)
        ran = random.randint(1, len(eles)-2)
        text = self.getText_element(eles[ran])
        while text.startswith('指纹锁'):
            ran = random.randint(1, len(eles) - 2)
            text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('选择【%s】' % text)

    # 联动条件二级界面
    def add_condition_next(self):
        eles = self.wait_for_elements(id='ci tick nor')
        ran = random.randint(0, len(eles)-1)
        self.click_element(eles[ran])
        res = self.element_attribute(eles[ran], 'value')
        suc = 0
        if res == '1':
            print('结果：条件选择成功')
        else:
            suc = 1
            print('结果：条件选择失败')
        return suc

    # 添加设备
    def add_devices_btn(self, num):
        time.sleep(2)
        eles = self.wait_for_elements(id='btn add n')
        self.click_element(eles[num])

    # 勾选全选
    def linkage_device_add(self):
        ele = self.wait_for_element(id='全选')
        self.click_element(ele)

    # 收起伸缩栏
    def click_bottom_btn(self,num):
        eles = self.findIpts(self.bottom_btn)
        self.click_element(eles[num])

    # 删除联动
    def delete_linkage(self):
        ele = self.wait_for_element(id='删除联动')
        while not ele:
            self.swipe_up_Big()
            ele = self.wait_for_element(id='删除联动')
        self.click_element(ele)
        ele = self.wait_for_element(id='删除后，无法控制该联动 确定删除?')
        suc = 0
        if ele:
            self.id_click('确定')
            print('结果：确定删除')
        else:
            suc = 1
            print('结果：没有删除弹出框')
        return suc