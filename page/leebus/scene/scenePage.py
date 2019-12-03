#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 上午11:24
# @Author  : Chenzd
# @Site    : 场景页面类
# @File    : scenePage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
from page.leebus.commonPage import CommonPage
class ScenePage(BasePage):

    #添加设备的勾选按钮
    chose = "ci tick nor"
    scene_icon = "type=='XCUIElementTypeImage'"
    StaticText = "type=='XCUIElementTypeStaticText'"
    scene_device = "type=='XCUIElementTypeStaticText' and visible==true"
    # 添加自定义场景
    def add_scene(self):
        self.id_click('添加')
        self.id_click('自定义场景')


    # 设备上限再勾选设备
    def add_device_by_chose(self):
        eles = self.wait_for_elements(id=self.chose)
        suc = 2
        for i in range(8):
            value = self.element_attribute(eles[i],'value')
            if not value:
                self.click_element(eles[i])
                value = self.element_attribute(eles[i], 'value')
                if not value:
                    suc = 0
                    print('结果：只能添加100个设备')
                else:
                    suc = 1
                    print('结果：场景设备超过100个')
        return suc

    # 循环遍历所有设备
    def add_advice_by_chose_for(self):
        res = self.add_device_by_chose()
        while res == 2:
            self.swipe_up()
            res = self.add_device_by_chose()
        return res

    # 随机选择场景图标
    def chonse_item_img(self):
        eles = self.findIpts(self.scene_icon)
        ran = random.randint(0,4)
        self.click_element(eles[ran])
        value = self.element_attribute(eles[ran], 'name')
        suc = 0
        if value == 'arming_border_sel':
            print('结果：选择场景图标成功')
        else:
            suc = 1
            print('结果：选择场景图标失败')
        return suc

    # 检测是否成功创建场景
    def check_creat_custom_scene(self):
        time.sleep(2)
        self.swipe_up()
        eles = self.findIpts(self.StaticText)
        text = self.getText_element(eles[-1])
        suc = 0
        if text == CommonPage.scene_name_list[-1]:
            print('结果：创建成功')
        else:
            suc = 1
            print('结果：创建失败')
        return suc

    # 创建场景--包含当前系统的各个类型------------------------------------------

    def click_add_device(self):
        eles = self.wait_for_elements(id='btn add n')
        self.click_element(eles[0])

    # 获取当前页设备列表名称
    index = 0
    def get_name_for_scene(self):
        eles = self.findIpts(self.StaticText)
        text_list = []
        flag = 0
        for i in range(2+self.index, len(eles)-1):
            res = self.element_attribute(eles[i], 'visible')
            if res == 'true':
                text = self.getText_element(eles[i])
                text_list.append(text)
            else:
                flag += 1
            if flag == 5:
                break
        self.index += 12
        return text_list

    # 各个类型添加一个
    def add_device_by_type(self):
        list = ['灯','窗帘','新风','调光','地暖','中央空调','电磁阀','推窗器','调色灯','双路通用',
                '机械手','声光报警器','单路通用','电视','智能插座']
        text_list1 = self.get_name_for_scene()
        for k1, v2 in enumerate(list):
            for k, v in enumerate(text_list1):
                if list[k1] in text_list1[k]:
                    ele = self.findIpt('name CONTAINS ("' + v + '") ')
                    self.click_element(ele)
                    print('添加设备类型【%s】' % v)
                    list.remove(list[k1])
                    if k1 == len(list): # 因为删除一个了，不用减一
                        break
        self.swipe_up()
        text_list2 = self.get_name_for_scene()
        while text_list1[-1] != text_list2[-1]:
            for k1, v2 in enumerate(list):
                for k, v in enumerate(text_list2):
                    if list[k1] in text_list2[k]:
                        ele = self.findIpt('name CONTAINS ("' + v + '") ')
                        self.click_element(ele)
                        print('添加设备类型【%s】' % v)
                        list.remove(list[k1])
                        if k1 == len(list):  # 因为删除一个了，不用减一
                            break
            self.swipe_up()
            self.swipe_down_small()
            text_list1 = self.get_name_for_scene()
            if len(text_list1) == 0:
                break
            for k1, v2 in enumerate(list):
                for k, v in enumerate(text_list1):
                    if list[k1] in text_list1[k]:
                        ele = self.findIpt('name CONTAINS ("' + v + '") ')
                        self.click_element(ele)
                        print('添加设备类型【%s】' % v)
                        list.remove(list[k1])
                        if k1 == len(list):  # 因为删除一个了，不用减一
                            break
            self.swipe_up()
            text_list2 = self.get_name_for_scene()
            if len(text_list2) == 0:
                break
            if len(list) == 0:
                print('所有类型添加完毕，退出循环')
                break
        else:
            print('结果：滑到底了')
        self.index = 0