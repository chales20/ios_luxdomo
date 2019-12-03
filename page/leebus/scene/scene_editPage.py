#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 下午1:41
# @Author  : Chenzd
# @Site    : 场景编辑页面类
# @File    : scene_editPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
class Scene_editPage(BasePage):
    StaticText = "type=='XCUIElementTypeStaticText'"
    TypeButton = "type=='XCUIElementTypeButton'"

    # 获取出编辑页面的设备名称
    def get_relate_text(self):
        eles = self.findIpts(self.StaticText)
        text_list = []
        delay_time = []
        device_name = []
        action_text = []
        if len(eles) > 29:
            for i in range(29):
                text_list.append(self.getText_element(eles[i]))
        else:
            for i in range(len(eles)):
                text_list.append(self.getText_element(eles[i]))
        text_list.pop(0)
        while text_list[1] != '立即':
            text_list.pop(0)
        for k, v in enumerate(text_list):
            if k%4 == 1:
                delay_time.append(text_list[k])
            if k%4 == 2:
                device_name.append(text_list[k])
            if k%4 == 3:
                action_text.append(text_list[k])
        return delay_time, device_name, action_text

    def get_relate_text2(self):
        eles = self.findIpts(self.StaticText)
        text_list = []
        delay_time = []
        device_name = []
        action_text = []
        for i in range(29,len(eles)):
            text_list.append(self.getText_element(eles[i]))
        if len(text_list) > 1:
            while text_list[1] != '立即':
                text_list.pop(0)
        for k, v in enumerate(text_list):
            if k%4 == 1:
                delay_time.append(text_list[k])
            if k%4 == 2:
                device_name.append(text_list[k])
            if k%4 == 3:
                action_text.append(text_list[k])
        return delay_time, device_name, action_text


    # 遍历获取出对应类型的文本进行操作
    index = []
    v = []
    def each_for(self, name):
        text = self.get_relate_text()
        device_name = text[1]
        suc = 0
        for k, v in enumerate(device_name):
            if device_name[k].startswith(name):
                ele = self.findIpts('name CONTAINS ("' + v + '") ')
                self.click_element(ele[0])
                self.v.append(v)
                self.index.append(k)
                suc = 1
                print('场景中编辑设备类型【%s】' % v)
                break
        if suc == 0:
            self.swipe_up_Big()
            text = self.get_relate_text2()
            device_name = text[1]
            for k, v in enumerate(device_name):
                if device_name[k].startswith(name):
                    ele = self.findIpts('name CONTAINS ("' + v + '") ')
                    self.click_element(ele[0])
                    self.index.append(k)
                    self.v.append(v)
                    suc = 1
                    print('场景中编辑设备类型【%s】' % v)
                    break
        return suc

    # 灯类型
    action_text = []
    action = []
    def light_type(self):
        self.action_text = []
        self.action = []
        eles = self.findIpts(self.StaticText)
        self.click_element(eles[5])
        eles = self.findIpts(self.TypeButton)
        eles_len = [eles[2],eles[3]]
        ran = random.randint(0,len(eles_len)-1)
        action = self.element_attribute(eles_len[ran], 'name')
        print('设置动作为【%s】' % action)
        self.action_text.append(action)
        self.click_element(eles_len[ran])
        if action.startswith('开'):
            ele = self.wait_for_element(id='延迟关闭')
            if not ele:
                print('结果：zigbee灯无延时关闭')
            else:
                self.click_element(ele)
                eles = self.findIpts(self.TypeButton)
                ran = random.randint(2,8)
                time = self.getText_element(eles[ran])
                print('设置延时关闭为【%s】' % time)
                if time !='无':
                    self.action_text.append(time)
                self.click_element(eles[ran])
        self.action.append(''.join(self.action_text))

    # 窗帘类型/新风类型
    curtains_text = []
    def curtains_type(self):
        self.curtains_text = []
        eles = self.findIpts(self.StaticText)
        ran = random.randint(4,len(eles)-1)
        text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('设置的执行动作为【%s】'% text)
        self.curtains_text.append(text)

    # 判断是否zigbee窗帘
    def leebus_or_zigbee(self, name):
        ele = self.wait_for_element(id=name)
        suc = 0
        if ele:
            print('********无线设备********')
            suc = 1
        else:
            print('********两线设备********')
        return suc

    # zigbee窗帘类型
    def zigbee_curtain_type(self):
        self.curtains_text = []
        eles = self.findIpts(self.StaticText)
        self.click_element(eles[-1])
        time.sleep(1)
        self.swipe_control(270, 389, 135, 389)
        time.sleep(1)
        eles = self.findIpts(self.StaticText)
        text1 = self.getText_element(eles[1])
        print('1.第一次滑动窗帘开启【%s】'% text1)
        self.swipe_control(135, 389, 270, 389)
        time.sleep(1)
        text2 = self.getText_element(eles[1])
        print('1.第二次滑动窗帘开启【%s】'% text2)
        self.id_click('确定')
        eles = self.findIpts(self.StaticText)
        text = self.getText_element(eles[-1])
        suc = 0
        if text in text2:
            print('调节位置后显示正确')
        else:
            suc = 1
            print('调节位置后显示错误')
        print('设置的执行动作为【%s】' % text)
        self.curtains_text.append(text)
        return suc

    # 调光灯类型
    dimmer_text = []
    def dimmer_type(self):
        self.dimmer_text = []
        eles = self.findIpts(self.StaticText)
        eles_list = [eles[4], eles[-1]]
        ran = random.randint(0, 1)
        text = self.getText_element(eles_list[ran])
        self.click_element(eles_list[ran])
        print('设置的执行动作为【%s】' % text)
        self.dimmer_text.append(text)

    # 下拉框类型
    select_text = []
    def select_type(self, ele, ran):
        self.click_element(ele)
        eles_action = self.findIpts(self.TypeButton)
        action = self.getText_element(eles_action[ran])
        print('设置为【%s】' % action)
        self.click_element(eles_action[ran])
        self.select_text.append(action)

    # 中央空调类型
    aircondition_text = []
    def aircondition_type(self):
        eles = self.findIpts(self.StaticText)
        ran = random.randint(2,3)
        self.select_type(eles[5],ran)
        if self.select_text[-1] == '开':
            ran = random.randint(2,5)
            self.select_type(eles[7],ran)
            ran = random.randint(2, 4)
            self.select_type(eles[9], ran)
            ran = random.randint(2, 12)
            self.select_type(eles[11], ran)
        self.aircondition_text.append(''.join(self.select_text))
        self.select_text = []

    # 地暖类型
    warm_text = []
    def warm_type(self):
        eles = self.findIpts(self.StaticText)
        ran = random.randint(2,3)
        self.select_type(eles[5], ran)
        if self.select_text[-1] == '开':
            ran = random.randint(2,12)
            self.select_type(eles[7],ran)
        self.warm_text.append(''.join(self.select_text))
        self.select_text = []

    # 调色灯类型
    palette_text = []
    def palette_type_scene(self):
        eles = self.findIpts(self.StaticText)
        ran = random.randint(2, 3)
        self.select_type(eles[3], ran)
        self.palette_text.append(''.join(self.select_text))
        self.select_text = []

    def palette_type_linkage(self):
        eles = self.findIpts(self.StaticText)
        ran = random.randint(2, 3)
        self.select_type(eles[5], ran)
        self.palette_text.append(''.join(self.select_text))
        self.select_text = []

    # 智能插座
    socket_text = []
    def socket_type(self):
        self.curtains_text = []
        eles = self.findIpts(self.StaticText)
        ran = random.randint(3, len(eles) - 1)
        text = self.getText_element(eles[ran])
        self.click_element(eles[ran])
        print('设置的执行动作为【%s】' % text)
        self.socket_text.append(text)

    # 对比另一页面灯显示是否与配置的一样
    def contrast_set(self,action_name):
        text = self.get_relate_text()
        device_name = text[1]
        suc = 0
        if self.v[-1] in device_name:
            action = text[2]
            name = action[self.index[-1]]
        else:
            text = self.get_relate_text2()
            action2 = text[2]
            name = action2[self.index[-1]]
        for i in list(action_name):
            if i not in name:
                suc = 1
                print('结果：页面显示文本与设置不同')
                break
        else:
            print('结果：页面显示文本与设置相同')

        return suc

    # 进入二级界面删除设备
    def delete_device(self):
        list = self.get_relate_text()
        deviceName = list[1]
        ran = random.randint(0, len(deviceName)-1)
        text = deviceName[ran]
        print('要删除的设备为【%s】' % text)
        ele = self.findIpts('name CONTAINS ("' + text + '") ')
        self.click_element(ele[0])
        self.id_click('删除')
        ele = self.wait_for_element(id='确定')
        if ele:
            eles = self.findIpts(self.StaticText)
            toast = self.getText_element(eles[0])
            print('弹出框内容为【%s】' % toast)
            self.click_element(ele)
        list = self.get_relate_text()
        deviceName = list[1]
        suc = 0
        if deviceName[ran] != text:
            print('结果：删除成功')
        else:
            suc = 1
            print('结果：删除失败')
        return suc

    # 回到最顶部
    def back_top(self):
        self.swipe_down()
        self.swipe_down()
        self.swipe_down()

    # 长按场景进入编辑页面
    def enter_sceneEt(self, name):
        eles = self.findIpts('name CONTAINS ("' + name + '")')
        text = self.element_attribute(eles[0], 'visible')
        while text == 'false':
            self.swipe_up_Big()
            text = self.element_attribute(eles[0], 'visible')
        time.sleep(1)
        self.longPress(eles[0])
        suc = 0
        ele = self.wait_for_element('编辑')
        if ele:
            self.click_element(ele)
            print('结果：长按进入编辑')
        else:
            suc = 1
            print('结果：长按没有菜单')
        return suc

    # 删除场景
    def delete_scene(self):
        ele = self.wait_for_element(id='删除场景')
        while not ele:
            self.swipe_up_Big()
            ele = self.wait_for_element(id='删除场景')
        self.click_element(ele)
        ele = self.wait_for_element(id='是否删除该场景?')
        suc = 0
        if ele:
            self.id_click('确定')
            print('结果：确定删除')
        else:
            suc = 1
            print('结果：没有删除弹出框')
        return suc






if __name__ == '__main__':
    b ='开1分钟'
    a = '开启1分钟后关闭'
    c = list(b)
    print(c)