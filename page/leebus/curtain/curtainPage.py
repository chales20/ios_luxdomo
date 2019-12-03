#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 下午2:49
# @Author  : Chenzd
# @Site    : 窗帘页面类
# @File    : curtainPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.basePage import BasePage
class CurtainPage(BasePage):

    # 逻辑窗帘名称
    curtain_name = "type == 'XCUIElementTypeStaticText'"
    # 配置窗帘，页面显示名称
    curtain_name_true ="type == 'XCUIElementTypeStaticText' and visible==true"
    # 隐藏按钮
    hide_btn = "type == 'XCUIElementTypeButton'"
    # zigbee窗帘的逻辑设备--配置
    zigbee_curtain_logic = "type == 'XCUIElementTypeImage' and name=='dm_pannel_nor'"
    # 窗帘时长的文本
    curtain_time = "type =='XCUIElementTypePickerWheel'"
    # 窗帘面板物理名称--随机获取
    def random_curtain_logicName(self):
        rlist = ['单路窗帘控制面板','双路窗帘控制面板']
        # rlist = ['双路窗帘控制面板f4']
        ran = random.randint(0, len(rlist)-1)
        return rlist[ran]

    '''判断窗帘类型'''
    def curtain_type(self):
        eles = self.findIpts(self.zigbee_curtain_logic)
        if eles:
            res = 0
            print('无线P1类型窗帘面板')
        else:
            res = 1
            print('两线类型窗帘面板')
        return res

    '''无线窗帘面板获取楼层信息'''
    def get_location(self):
        CommonPage(self.driver).enter_menu()
        location = self.getText_element(self.findIpts(CommonPage.device_location_physical)[1])
        self.id_click('保存')
        time.sleep(2)
        return location

    hide_text = []
    location_text = []
    # 根据窗帘物理设备名称判断类型进行不同操作
    def curtain_type_defferent_operation(self):
        eles_name = self.findIpts(self.curtain_name)
        text = self.getText_element(eles_name[0])
        if text.startswith('ZigBee'):
            print('ZigBee窗帘配置')
            suc = 0
            location = self.get_location()
            self.location_text.append(location)
            eles = self.findIpts(self.zigbee_curtain_logic)
            ran = random.randint(0,len(eles)-1)
            self.click_element(eles[ran])

        else:
            if text.startswith('双路'):
                eles_btn = self.findIpts(self.hide_btn)
                btn_list = [eles_btn[4], eles_btn[-1]]
                text1 = self.getText_element(eles_name[2])
                location = self.getText_element(eles_name[3])
                text2 = self.getText_element(eles_name[4])
                location2 = self.getText_element(eles_name[5])
                text_list = [text1,text2]
                location_list = [location,location2]
                ran = random.randint(0,len(btn_list)-1)
                self.click_element(btn_list[ran])
                self.hide_text.append(text_list[ran])
                self.location_text.append(location_list[ran])
                print('隐藏窗帘名称【%s】'%text_list[ran])
            elif text.startswith('单路'):
                eles_btn = self.findIpts(self.hide_btn)
                text1 = self.getText_element(eles_name[2])
                location = self.getText_element(eles_name[3])
                self.click_element(eles_btn[-1])
                self.hide_text.append(text1)
                self.location_text.append(location)
                print('隐藏窗帘名称【%s】' % text1)
            ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
            suc = 0
            if ele:
                self.id_click('确定')
            else:
                suc = 1
                print('未弹出确认框')
            self.id_click('返回')
            self.id_click('返回')
            self.id_click('家')
        return suc

    # 若是两线窗帘进行检测隐藏，若是zigbee窗帘，则进行配置
    def curtain_operation(self):
        if len(self.hide_text) > 0:
            print('在主页遍历所有设备名称查看是否隐藏')
            CommonPage(self.driver).enter_room_for_hide_logic(self.location_text[-1])
            result = CommonPage(self.driver).find_deviceName(self.hide_text[-1])
            return result
        else:
            eles = self.findIpts(self.curtain_name_true)
            if len(eles)>2:
                ran = random.randint(2,len(eles)-1)
                text = self.getText_element(eles[ran])
                self.click_element(eles[ran])
                print('配置窗帘名称为【%s】'%text)
                self.id_click('保存')
                eles = self.findIpts(self.curtain_name)
                text_list = []
                suc = 0
                for i in eles:
                    text_list.append(self.getText_element(i))
                if text in text_list:
                    print('结果：zigbee窗帘面板配置成功')
                    print('取消窗帘配置')
                    self.id_click(text)
                    self.id_click(text)
                    self.id_click('保存')
                    time.sleep(1)
                    self.id_click('barItem back n')
                    self.id_click('返回')
                    self.id_click('家')
                else:
                    suc = 1
                    print('结果：zigbee窗帘配置异常')
                return suc
            else:
                print('无窗帘设备可配置,返回到首页')
                self.id_click('返回')

    # 若self.hide_text = [] 不为空，则进行取消隐藏，否则pass
    def cancle_hide_curtain(self, logicName):
        CommonPage(self.driver).back_top()
        CommonPage(self.driver).enter_device_list('窗帘控制面板', logicName)
        eles_btn = self.findIpts(self.hide_btn)
        hide_btn = [eles_btn[4],eles_btn[-1]]
        for i in hide_btn:
            self.click_element(i)
            ele = self.wait_for_element(id='隐藏后控制界面不显示该设备,是否隐藏?')
            if ele:
                self.id_click('取消')
            else:
                print('结果：取消隐藏成功')
                break
        self.id_click('返回')
        self.id_click('返回')
        self.id_click('家')


    '''
    主界面设备编辑类###############################################################
    '''
    def set_time(self):
        eles = self.findIpts(self.curtain_name)
        self.click_element(eles[5])
        ele = self.wait_for_element(id='确定')
        if ele:
            ele_text = self.findIpt(self.curtain_time)
            time_text= self.getText_element(ele_text)
            if time_text == '60':
                self.swipe_down_small()
            else:
                self.swipe_up_small()
            time_text = self.getText_element(ele_text)
            print('设置的窗帘时长为【%s秒】'%time_text)
            self.id_click('确定')
            text = self.getText_element(eles[5])
            suc = 0
            if text == time_text:
                print('结果：设置窗帘时长成功')
            else:
                suc = 1
                print('结果：设置窗帘时间失败')
        else:
            suc = 1
            print('无弹出框')
        return suc

    '''
    窗帘控制页面类################################################################
    '''

    def control_curtain(self,action):
        print('1. 点击[%s]，判断是否控制成功'% action)
        self.id_click(action)
        time.sleep(1)
        ele = self.wait_for_element(id=action)
        text = self.element_attribute(ele, 'value')
        suc = 0
        if text == '1':  # 选中的值为1
            print('结果：控制成功')
        else:
            suc = 1
            print('结果：控制失败')
        return suc