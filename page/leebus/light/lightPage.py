#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/15 下午2:41
# @Author  : Chenzd
# @Site    : 灯的页面类
# @File    : lightPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time
from page.appiumDriver import MyDriver
from page.basePage import BasePage
from page.leebus.commonPage import CommonPage


class LightPage(BasePage):

    roomNameEdit = "type=='XCUIElementTypeTextField'"

    # 开关逻辑设备
    logicPanel = "type == 'XCUIElementTypeStaticText'"

    # 窗帘图标
    curtain_img = "0-2-0-0-0"
    # 灯图标
    light_img = "0-10-0-0-0"
    # 电磁阀图标
    solenoidvalue_img = "0-25-0-0-0"
    # 机械手
    manipulator_img = "0-28-0-0-0"
    # 门
    door_img = "0-27-0-0-0"

    # 按键控制其它设备
    control_other_btn = "type=='XCUIElementTypeSwitch'"
    device_name_show = "type=='XCUIElementTypeStaticText'"  # 移动到--房间名称也调用次方法

    #隐藏按钮
    hide_btn = "type=='XCUIElementTypeButton' and name=='dm tick nor'"

    # 页面顶栏房间名称
    nav_Bar = "type=='XCUIElementTypeButton'"


    '''
    灯物理设备页面类########################################################################
    '''

    # 开关面板物理名称--随机获取
    def random_light_logicName(self):
        rlist = ['1路智能开关面板', '2路智能开关面板', '3路智能开关面板', '4路智能开关面板']
        # rlist = ['2路智能开关面板9328']
        ran = random.randint(0, len(rlist)-1)
        return rlist[ran]

    # '''房间楼层配置方法'''
    # def floorRoomConfig_is_normal(self):
    #     print('1.点击房间楼层进入楼层房间配置页')
    #     time.sleep(5)
    #     self.id_click('楼层房间配置')
    #     print('2.添加默认楼层的30个房间')
    #     for i in range(30):
    #         self.waitEle_for_down('添加房间')
    #         self.id_click('添加房间')
    #         self.input(self.findIpt(self.roomNameEdit), "房间"+str(i+1))
    #         self.id_click('保存')
    #     print('3.添加楼层')
    #     for i in range(5):
    #         self.waitEle_for_down('添加楼层')
    #         self.id_click('添加楼层')
    #         self.input(self.findIpt(self.roomNameEdit), str(i+2)+'楼')
    #         self.id_click('保存')
    #     print('4.收起默认楼层展开栏')
    #     self.id_click('返回')
    #     self.waitEle_for_down('楼层房间配置')
    #     self.id_click('楼层房间配置')
    #     self.id_click('1楼')
    #     print('5.添加2楼房间')
    #     self.id_click('添加房间')
    #     self.input(self.findIpt(self.roomNameEdit),'房间31')
    #     self.id_click('保存')
    #     print('房间楼层配置功能验证通过')
    #     self.id_click('返回')

    '''
    灯逻辑设备页面类#####################################################################
    '''

    enter_text = []
    '''进入灯的逻辑设备'''
    def enter_light_logic(self):
        rlist = self.findIpts(self.logicPanel)
        ran = random.randint(1, len(rlist)-1)
        text = self.getText_element(rlist[ran])
        self.enter_text.append(text)
        self.click_element(rlist[ran])


    '''P1面板配置'''
    def config_P1(self):
        eles = self.findIpts(self.device_name_show)
        ran = random.randint(3, 9)
        device_name = self.getText_element(eles[ran - 1])
        self.click_element(eles[ran - 1])
        print('2.选择控制的设备名称为【%s】' % device_name)
        self.id_click('保存')
        eles = self.findIpts(self.device_name_show)
        print('3.获取出物理设备页所有文本信息')
        test_list = []
        for i in range(len(eles) - 1):
            text = self.getText_element(eles[i])
            test_list.append(text)
        print('4.判断选择的设备文本是否在物理设备页显示')
        suc = 0
        if device_name in test_list:
            print('结果：P1面板配置成功')
        elif self.enter_text[0] == device_name:
            print('结果：P1面板配置成功')
        else:
            suc = 1
            print('结果：P1面板配置失败')
        self.enter_text = []
        return suc

    '''判断进入逻辑设备后的界面'''
    def enter_light_logic_type(self):
        time.sleep(2)
        ele = self.wait_for_element(id='ci loc nor')
        suc = 0
        if ele:
            print('【处于逻辑灯编辑界面】')
        else:
            suc = 1
            print('【处于P1面板灯配置界面】')
        return suc

    '''图标替换'''
    def icon_replace(self):
        self.id_click('图标')
        print('1.进入图标替换列表')
        icon_list = [self.curtain_img,self.solenoidvalue_img,self.door_img,self.manipulator_img]
        ran = random.randint(0,len(icon_list)-1)
        self.id_click(icon_list[ran])
        print('2.随机选择一个图标')
        suc = 0
        eles = self.wait_for_elements(id=icon_list[ran])
        print('3.判断图标替换是否成功')
        if len(eles)==2:
            print('结果：图标替换正常')
        else:
            suc = 1
            print('结果：图标替换异常')
        ele = self.wait_for_elements(id=self.light_img)
        self.click_element(ele[-1])
        self.id_click('返回')
        return suc

    device_text = []
    '''按键控制其它设备'''
    def control_other(self):
        self.click_element(self.findIpt(self.control_other_btn))
        eles = self.findIpts(self.device_name_show)
        self.click_element(eles[-1])
        print('1.进入设备选择列表')
        eles = self.findIpts(self.device_name_show)
        ran = random.randint(3, 9)
        self.click_element(eles[ran-1])
        device_name = self.getText_element(eles[ran-1])
        print('2.选择控制的设备名称为【%s】'% device_name)
        self.device_text.append(device_name)
        self.id_click('保存')
        time.sleep(2)
        self.id_click('保存')
        eles = self.findIpts(self.device_name_show)
        print('3.获取出物理设备页所有文本信息')
        test_list = []
        for i in range(len(eles)-1):
            text = self.getText_element(eles[i])
            test_list.append(text)
        print('4.判断选择的设备文本是否在物理设备页显示')
        suc = 0
        if device_name in test_list:
            print('结果：按键控制其它设备正常')
        elif self.enter_text[0] == device_name:
            print('结果：按键控制其它设备正常')
        else:
            suc = 1
            print('结果：按键控制其它设备异常')
        self.enter_text = []  # 制空，不影响下次调用
        return suc

    '''根据按键控制其它设备的设备名称，点击回去逻辑设备页面'''
    def enter_logic_by_name(self):
        self.id_click(self.device_text[0])
        self.device_text = []  # 制空不影响下次调用


    '''关闭按键控制其它设备'''
    def close_control_other(self):
        ele = self.findIpt(self.control_other_btn)
        self.click_element(ele)
        time.sleep(1)
        self.id_click('2楼')

    '''获取逻辑设备名称'''
    def get_logicName(self):
        ele = self.findIpt(self.roomNameEdit)
        text = self.getText_element(ele)
        if len(text) < 7:
            return text
        else:
            return text[0:8]

    logic_device_name = []
    '''隐藏功能是否正常'''
    def Hide_is_normal(self):
        time.sleep(2)
        ele = self.findIpt(self.roomNameEdit)
        text = self.getText_element(ele)
        print('1. 获取逻辑设备的名称【%s】'% text)
        self.logic_device_name.append(text)
        self.click_element(self.findIpt(self.hide_btn))
        print('1.勾选隐藏')
        ele = self.wait_for_element(id='隐藏后控制界面不显示该设备，是否隐藏？')
        if ele:
            self.id_click('确定')
        else:
            print('未弹出确认框')
        print('2.返回主界面对比')
        self.id_click('保存')
        time.sleep(2)
        self.id_click('返回')
        self.id_click('返回')
        self.id_click('家')
        time.sleep(2)
        self.enter_room_for_hide(CommonPage.default_roomName[-1])
        result = CommonPage(self.driver).find_deviceName(text)
        return result

    # 进入对应的隐藏设备房间
    def enter_room_for_hide(self, roomName):
        eles = self.findIpts(CommonPage.title_roomName)
        self.click_element(eles[-2])
        if roomName.startswith(' '):
            name = roomName.replace(' ','')
            eles = self.findIpts("name CONTAINS '" + name + "'")
        else:
            eles = self.findIpts("name CONTAINS '" + roomName + "'")
        self.click_element(eles[0])
        ele = self.findIpt(CommonPage.city)
        if not ele:
            CommonPage(self.driver).back()

    '''取消隐藏'''
    def cancle_hide(self):
        self.id_click(self.logic_device_name[0])
        self.waitEle_for_down('按键控制其它设备')
        self.click_element(self.findIpt(self.hide_btn))
        self.id_click('保存')
        self.id_click('返回')
        self.id_click('返回')
        self.id_click('家')
        CommonPage.floor_name = []

    '''
    灯主界面编辑页面类#####################################################################
    '''
    '''获取主界面屏幕内设备名称'''
    def find_deviceName_interface(self):
        rlist = []
        deviceName_list = self.findIpts(self.device_name_show)
        for i in deviceName_list:
            res = self.findElement_for_interface(i)
            if res is True:
                text = self.getText_element(i)
                rlist.append(text)
        return rlist

    '''设备类型--传入名称查找对应设备类型名字'''
    def light_interface(self, name):
        rlist = self.find_deviceName_interface()
        text_list = []
        for i in rlist:
            if name in i:
                text_list.append(i)
        return text_list

    '''随机长按设备--根据参数判断'''
    def random_longPress_light(self, name):
        text_list = self.light_interface(name)
        while len(text_list) == 0:
            self.swipe_up_Big()
            text_list = self.light_interface(name)
        ran = random.randint(0, len(text_list) - 1)
        print('随机长按设备【%s】' % text_list[ran])
        ele = self.wait_for_element(id=text_list[ran])
        self.longPress(ele)

    def random_longPress(self, name):
        ele = self.findIpt('name CONTAINS("'+name+'")')
        i = 0
        while not ele:
            if i < 10:
                i += 1
                self.swipe_up_Big()
                ele = self.findIpt('name CONTAINS("'+name+'")')
            else:
                break
        self.waitEle_for_down_by_ele(ele)
        self.longPress(ele)

    '''长按指定名称设备'''
    def longPress_text(self, name):
        ele = self.findIpt("name CONTAINS '" + name + "'")
        while not ele:
            self.swipe_up_Big()
            ele = self.findIpt("name CONTAINS '" + name + "'")
        res = self.findElement_for_interface(ele)
        while not res:
            self.swipe_up()
            res = self.findElement_for_interface(ele)
        self.longPress(ele)

    '''随机点击设备--根据参数判断'''
    def click_device_interface(self, name):
        ele = self.findIpt('name CONTAINS("' + name + '")')
        i = 0
        while not ele:
            if i < 10:
                self.swipe_up_Big()
                ele = self.findIpt('name CONTAINS("' + name + '")')
                i += 1
            else:
                break
        self.swipe_up_small()
        self.waitEle_for_down_by_ele(ele)
        self.click_element(ele)

    '''移动到'''
    def move_to(self, name):
        eles = self.findIpts(self.device_name_show)
        ran = random.randint(3,9)
        text = self.getText_element(eles[ran])
        while name in text:
            ran = random.randint(3, 9)
            text = self.getText_element(eles[ran])
        print('随机选择当前房间列的房间【%s】'%text)
        self.click_element(eles[ran])
        time.sleep(2)
        eles = self.findIpts(self.nav_Bar)
        Bar_name = self.element_attribute(eles[-2], 'name')
        suc = 0
        if text==Bar_name:
            print('结果：移动到功能正常')
        else:
            suc = 1
            print('结果：移动到功能异常')
        return suc

    '''移动回初始房间'''
    def move_to_defaule(self, name):
        ele = self.findIpt('name CONTAINS("'+name+'")')
        self.click_element(ele)



    '''
    主界面控制页面类####################################################
    '''

    def control_light(self):
        already_text = []  # 已经控制过的灯名称
        text_light = self.find_deviceName_interface()
        while text_light[-1]!='其它设备' and text_light[-1] != '传感器':
            deff_text = [x for x in text_light if x not in already_text]
            for i in deff_text:
                if i.startswith('灯'):
                    self.id_click(i)
                    already_text.append(i)
            self.swipe_up_Big()
            text_light = self.find_deviceName_interface()
        else:
            deff_text = [x for x in text_light if x not in already_text]
            for i in deff_text:
                if i.startswith('灯'):
                    self.id_click(i)
                    already_text.append(i)
            print('主界面所有灯控制结束')





if __name__ == '__main__':
    LightPage(MyDriver.cur_driver()).waitEle_for_down('楼层房间配置')
