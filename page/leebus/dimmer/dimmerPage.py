#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 上午9:57
# @Author  : Chenzd
# @Site    : 调光灯页面类
# @File    : dimmerPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage


class DimmerPage(BasePage):

    # 逻辑调光名称
    dimmer_name = "type == 'XCUIElementTypeStaticText'"
    # 隐藏按钮
    hide_btn = "type == 'XCUIElementTypeButton'"
    #前沿调光按钮
    before_dimmer_btn = "type=='XCUIElementTypeSwitch'"

    hide_text = []
    location_text = []
    # 调光灯隐藏
    def dimmer_hide_click(self):
        name_ele = self.findIpts(self.dimmer_name)
        hide_ele = self.findIpts(self.hide_btn)
        text1 = self.getText_element(name_ele[2])
        text2 = self.getText_element(name_ele[3])
        self.click_element(hide_ele[-1])
        self.hide_text.append(text1)
        self.location_text.append(text2)
        print('隐藏设备名称【%s】' % text1)
        ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
        suc = 0
        if ele:
            self.id_click('确定')
        else:
            suc = 1
            print('未弹出确认框')
        time.sleep(2)
        self.id_click('返回')
        self.id_click('返回')
        self.id_click('家')
        return suc

    # 隐藏----无面板控制以下设备文字

    def hide_click_have3ele(self):
        name_ele = self.findIpts(self.dimmer_name)
        hide_ele = self.findIpts(self.hide_btn)
        text1 = self.getText_element(name_ele[1])
        text2 = self.getText_element(name_ele[2])
        self.click_element(hide_ele[-1])
        self.hide_text.append(text1)
        self.location_text.append(text2)
        print('隐藏设备名称【%s】' % text1)
        ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
        suc = 0
        if ele:
            self.id_click('确定')
        else:
            suc = 1
            print('未弹出确认框')
        time.sleep(2)
        self.id_click('返回')
        self.id_click('返回')
        self.id_click('家')
        return suc

    # 主页检测是否隐藏成功
    def dimmer_hide_normal(self):
        if len(self.hide_text) > 0:
            CommonPage(self.driver).enter_room_for_hide_logic(self.location_text[-1])
            print('在主页遍历所有设备名称查看是否隐藏')
            result = CommonPage(self.driver).find_deviceName(self.hide_text[-1])
            return result

    # 取消隐藏
    def cancle_hide_dimmer(self,physicaiName,logicName):
        if len(self.hide_text) > 0:
            CommonPage(self.driver).enter_device_list(physicaiName, logicName)
            eles = self.findIpts(self.hide_btn)
            for i in range(3, len(eles)):
                self.click_element(eles[i])
                ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
                if ele:
                    self.id_click('取消')
            self.id_click('返回')
            self.id_click('返回')
            self.id_click('家')

    # 取消隐藏
    def cancle_hide_dimmer_nextPage(self, physicaiName, logicName):
        if len(self.hide_text) > 0:
            CommonPage(self.driver).enter_device_list_nextPage(physicaiName, logicName)
            eles = self.findIpts(self.hide_btn)
            for i in range(3, len(eles)):
                self.click_element(eles[i])
                ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
                if ele:
                    self.id_click('取消')
            self.id_click('返回')
            self.id_click('返回')
            self.id_click('家')


    #  判段是否有前沿调光按钮，有进行操作，无就跳过
    def is_dimmer_btn(self):
        self.swipe_up()
        ele = self.findIpt(self.before_dimmer_btn)
        if ele:
            attr1 = self.element_attribute(ele,'value')
            self.click_element(ele)
            attr2 = self.element_attribute(ele,'value')
            suc = 0
            if attr1 != attr2:
                print('结果：前沿调光控制成功')
            else:
                suc = 1
                print('结果：前沿调光控制失败')
            eles = self.findIpts(self.dimmer_name)
            self.click_element(eles[8])
            eles = self.findIpts(self.dimmer_name)
            text1 = self.getText_element(eles[1])
            self.swipe_control(98, 369, 270, 369)
            text2 = self.getText_element(eles[1])
            self.swipe_control(270, 369, 98, 369)
            self.id_click('确定')
            if text1 != text2:
                print('结果：滑动控制成功')
            else:
                suc = 1
                print('结果：滑动控制异常')
            return suc
        else:
            suc = 0
            print('结果：无前沿调光，跳过')
            return suc

    '''
    调光控制页面类##########################################################################
    '''
    # 调光灯btn图标
    dimmer_control_btn = 'dc_dl_box_nor'
    # 调光滑条
    dimmer_bar = "type=='XCUIElementTypeSlider'"

    # 调光开
    def control_dimmer_open(self):
        ele = self.wait_for_element(id=self.dimmer_control_btn)
        self.click_element(ele)
        time.sleep(2)
        ele_bar = self.findIpt(self.dimmer_bar)
        suc = 0
        if ele_bar:
            print('结果：控制成功')
        else:
            suc = 1
            print('结果：控制失败')
        return suc

    # 调光关
    def control_dimmer_close(self):
        ele = self.wait_for_element(id=self.dimmer_control_btn)
        self.click_element(ele)
        time.sleep(2)
        ele_bar = self.findIpt(self.dimmer_bar)
        suc = 0
        if ele_bar:
            suc = 1
            print('结果：控制失败')
        else:
            print('结果：控制成功')
        return suc

if __name__ == '__main__':
    list = [1, 2, 3]
    for i in range(2, len(list)):
        print(i)