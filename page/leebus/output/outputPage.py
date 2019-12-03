#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午3:41
# @Author  : Chenzd
# @Site    : 4路输出模块页面类
# @File    : outputPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
class OutputPage(BasePage):

    # 四路输出显示对文本按钮
    TypeButton = "type=='XCUIElementTypeButton'"
    # 配置对设备类型列表
    StaticText = "type=='XCUIElementTypeStaticText'"
    # 设备名称及位置
    TextField = "type=='XCUIElementTypeTextField'"

    # ----------配置------------
    deviceName = []
    def output_config(self, location_ele):
        eles_list = self.findIpts(location_ele)
        if len(eles_list)==9:
            ran_chose = random.randint(1,len(eles_list)-1)
        else:
            ran_chose = random.randint(3,len(eles_list)-1)
        self.click_element(eles_list[ran_chose])
        print('1.随机选择一个逻辑面板')
        eles = self.findIpts(self.TypeButton)
        self.click_element(eles[2])
        print('2.获取设备类型列表再随机选择一个')
        eles = self.findIpts(self.StaticText)
        ran = random.randint(1, len(eles)-1)
        typename = self.getText_element(eles[ran])
        print('3.选择【%s】' % typename)
        self.click_element(eles[ran])
        CommonPage(self.driver).save()
        eles = self.findIpts(self.TextField)
        device = self.getText_element(eles[0])
        self.deviceName.append(device)
        CommonPage(self.driver).save()
        time.sleep(2)
        ele = self.wait_for_element(id='返回')
        if not ele:
            eles = self.findIpts(self.StaticText)
            text1 = self.getText_element(eles[0])
            print('弹出框的消息内容：【%s】' % text1)
            self.id_click('确定')
        time.sleep(4)
        el_list = self.findIpts(location_ele)
        el_list.pop(0)
        suc = 2
        for i in el_list:
            text_show = self.element_attribute(i, 'name')
            if device[0:4] in text_show:
                suc = 0
                print('结果：配置成功')
                break
        if suc != 0:
            suc = 1
            print('结果：配置失败')
        self.click_element(eles_list[ran_chose])
        return suc

    # --------控制-----------
    def output_control_type(self):
        type_name = self.deviceName[-1]
        name_list_one = ['灯', '电磁阀', '声光报警器', '单路通用']
        name_list_two = ['窗帘', '推窗器', '机械手', '双路通用']
        for k, v in enumerate(name_list_one):
            if name_list_one[k] in type_name:
                suc = 0
                # 执行单点击操作
                LightPage(self.driver).click_device_interface(type_name)
                print('结果：【%s】控制成功' % type_name)
                return suc
        for k, v in enumerate(name_list_two):
            if name_list_two[k] in type_name:
                suc = 1
                # 执行有二级界面的操作
                LightPage(self.driver).click_device_interface(type_name)
                return suc

if __name__ == '__main__':
    a = 'ad'
    b = ['a','v', 'for']
    print(a in b)