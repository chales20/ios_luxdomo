#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 下午1:42
# @Author  : Chenzd
# @Site    : 多功能配置面板页面类
# @File    : scenePanelPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
class ScenePanelPage(BasePage):

    text_list = "type == 'XCUIElementTypeStaticText'"

    # 配置设备
    def config_device(self):
        time.sleep(1)
        eles = self.findIpts(self.text_list)
        ran = random.randint(1,len(eles)-1)
        enter_text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('进入随机一个面板')
        eles = self.findIpts(self.text_list)
        ran = random.randint(3, 9)
        device_name = self.getText_element(eles[ran - 1])
        self.click_element(eles[ran - 1])
        print('2.选择控制的设备名称为【%s】' % device_name)
        self.id_click('保存')
        eles = self.findIpts(self.text_list)
        print('3.获取出物理设备页所有文本信息')
        test_list = []
        for i in range(len(eles) - 1):
            text = self.getText_element(eles[i])
            test_list.append(text)
        print('4.判断选择的设备文本是否在物理设备页显示')
        suc = 0
        if device_name in test_list:
            print('结果：多功能面板配置成功')
        elif enter_text == device_name:
            print('结果：多功能面板配置成功')
        else:
            suc = 1
            print('结果：多功能面板配置失败')
        return suc

    # 配置场景
    def config_scene(self):
        eles = self.findIpts(self.text_list)
        ran = random.randint(1, len(eles) - 1)
        enter_text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('进入随机一个面板')
        self.waitEle_for_down('全开')
        self.swipe_up_Big()
        eles = self.findIpts(self.text_list)
        list_ele = [eles[-1],eles[-2]]
        ran = random.randint(0,len(list_ele)-1)
        device_name = self.getText_element(list_ele[ran])
        self.waitEle_for_down_by_ele(list_ele[ran])
        self.click_element(list_ele[ran])
        print('2.选择控制的场景名称为【%s】' % device_name)
        self.id_click('保存')
        eles = self.findIpts(self.text_list)
        print('3.获取出物理设备页所有文本信息')
        test_list = []
        for i in range(len(eles) - 1):
            text = self.getText_element(eles[i])
            test_list.append(text)
        print('4.判断选择的设备文本是否在物理设备页显示')
        suc = 0
        if device_name in test_list:
            print('结果：多功能面板配置成功')
        elif enter_text == device_name:
            print('结果：多功能面板配置成功')
        else:
            suc = 1
            print('结果：多功能面板配置失败')
        return suc