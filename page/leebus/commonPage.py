#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 上午11:15
# @Author  : Chenzd
# @Site    : 公共页面类
# @File    : commonPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

from page.basePage import BasePage
from selenium.webdriver.common.by import By
class CommonPage(BasePage):

    # 设备管理
    deviceLayout = "type=='XCUIElementTypeStaticText' and name=='设备管理'"
    # 名称编辑
    edit = "type=='XCUIElementTypeTextField' and enabled==true"
    # 物理设备位置
    device_location_physical = "type='XCUIElementTypeTextField'"
    # 逻辑设备位置
    device_location_logic = "type =='XCUIElementTypeStaticText'"
    # 逻辑设备楼层名称
    floor_logic = (By.XPATH, "//XCUIElementTypeCollectionView[1]//XCUIElementTypeStaticText")
    # 房间名称
    roomName = "type =='XCUIElementTypeStaticText'"
    # 物理设备标题
    title = "type == 'XCUIElementTypeStaticText'"
    # 物理编辑设备按钮
    button = "type=='XCUIElementTypeButton'"
    # 主页标题房间
    title_roomName = "type=='XCUIElementTypeButton'"
    # 厦门集美定位
    city = "type=='XCUIElementTypeStaticText' and name='厦门 · 集美'"
    top = "厦门 · 集美"


    # 进入设备管理选择设备到通用方法
    def enter_device_list(self,physical_name,logic_name):
        '''
        :param physical_name: 物理设备名称
        :param logic_name: 逻辑设备名称---可以输入前几个文字（模糊定位）
        :return:
        '''
        self.id_click('更多')
        self.click_element(self.findIpt(self.deviceLayout))
        time.sleep(1)
        ele = self.findIpts("name CONTAINS '" + physical_name + "'")
        i = 0
        while not ele:
            self.swipe_up()
            i += 1
            if i == 5:
                break
            ele = self.findIpts("name CONTAINS '" + physical_name + "'")
        # ran = random.randint(0, len(ele) - 1)
        self.click_element(ele[0])
        eles = self.findIpts("name CONTAINS '" + logic_name + "'")
        while not eles:
            self.swipe_down()
            eles = self.findIpts("name CONTAINS '" + logic_name + "'")
        ran = random.randint(0, len(eles) - 1)
        result = self.findElement_for_interface(eles[ran])
        while not result:
            self.swipe_down()
            result = self.findElement_for_interface(eles[ran])
        self.click_element(eles[ran])
        time.sleep(1)

    # 进入设备管理选择设备到通用方法--换页面
    def enter_device_list_nextPage(self,physical_name,logic_name):
        '''
        :param physical_name: 物理设备名称
        :param logic_name: 逻辑设备名称---可以输入前几个文字（模糊定位）
        :return:
        '''
        self.id_click('更多')
        self.click_element(self.findIpt(self.deviceLayout))
        time.sleep(1)
        eles = self.findIpts("name CONTAINS '" + physical_name + "'")
        i = 0
        while not eles:
            self.swipe_up()
            i += 1
            if i == 5:
                break
            eles = self.findIpts("name CONTAINS '" + physical_name + "'")
        # ran = random.randint(0, len(ele) - 1)
        self.click_element(eles[-1])
        eles = self.findIpts("name CONTAINS '" + logic_name + "'")
        while not eles:
            self.swipe_down()
            eles = self.findIpts("name CONTAINS '" + logic_name + "'")
        ran = random.randint(0, len(eles) - 1)
        result = self.findElement_for_interface(eles[ran])
        while not result:
            self.swipe_down()
            result = self.findElement_for_interface(eles[ran])
        self.click_element(eles[ran])
        time.sleep(1)

    # 进入设备管理选择设备到通用方法--随机
    physical_device = []
    def enter_device_list_random(self, physical_name, logic_name):
        '''
        :param physical_name: 物理设备名称
        :param logic_name: 逻辑设备名称---可以输入前几个文字（模糊定位）
        :return:
        '''
        self.id_click('更多')
        self.click_element(self.findIpt(self.deviceLayout))
        time.sleep(1)
        eles = self.findIpts("name CONTAINS '" + physical_name + "'")
        i = 0
        while not eles:
            self.swipe_up_Big()
            i += 1
            if i == 5:
                break
            eles = self.findIpts("name CONTAINS '" + physical_name + "'")
        ran = random.randint(0, len(eles) - 1)
        text = self.getText_element(eles[ran])
        print('【%s】' % text)
        self.physical_device.append(text)
        self.click_element(eles[ran])
        time.sleep(1)
        eles = self.findIpts("name CONTAINS '" + logic_name + "'")
        ran = random.randint(0, len(eles) - 1)
        result = self.findElement_for_interface(eles[ran])
        while not result:
            self.swipe_down()
            result = self.findElement_for_interface(eles[ran])
        self.click_element(eles[ran])
        time.sleep(1)

    # 进入...界面
    def enter_menu(self):
        self.id_click('id more nor')

    # 获取设备标题名称以便取消隐藏时，调用定位
    title_text = []
    def get_title(self):
        eles = self.findIpts(self.title)
        text = self.getText_element(eles[0])
        self.title_text.append(text)

    # 随机编辑设备名称
    def random_name(self):
        str_name = ['1','2','3','4','5','a','b','c','d','e','f','你','我','他','黑','豹','鸽']
        str_sum = []
        for i in range(21):
            a = str_name[random.randint(0,len(str_name)-1)]
            str_sum.append(a)
        name = ''.join(str_sum)
        return name

    update_name = []
    # 编辑设备名称，空，上限（中英文）
    def edit_name(self, first_edit, second_edit,save_name, name_exit):
        ele = self.findIpt(self.edit)
        text = self.getText_element(ele)
        self.input(self.findIpt(self.edit), first_edit)
        print('1.输入名称为空')
        self.id_click(save_name)
        ele = self.wait_for_element(name_exit)
        suc = 0
        if not ele:
            print('结果：空名称无法保存')
        else:
            suc = 1
            print('结果:空名称可以保存！错误！')
            return suc
        print('2.输入名称上限（包含数字、英文、中文）')
        if text.startswith('ZigBee'):
            str = 'ZigBee'.strip().replace(' ','')
            self.input(self.findIpt(self.edit),str)
            self.notclear_input(self.findIpt(self.edit), second_edit)
        else:
            self.input(self.findIpt(self.edit), second_edit)
        text = self.getText_element(self.findIpt(self.edit))
        self.update_name.append(text)
        print('编辑后的新名称为【%s】'%text)
        self.id_click(save_name)
        ele = self.wait_for_element(name_exit)
        suc = 0
        if ele:
            print('结果：名称上限可以保存（中/英/数字）')
        else:
            suc = 1
            print('结果:保存失败')
        return suc

    # 编辑场景名称
    scene_name_list = []
    def edit_name_scene(self, first_edit, second_edit,save_name, name_exit):
        ele = self.findIpt(self.edit)
        text = self.getText_element(ele)
        self.input(self.findIpt(self.edit), first_edit)
        print('1.输入名称为空')
        self.id_click(save_name)
        ele = self.wait_for_element(name_exit)
        suc = 0
        if not ele:
            print('结果：空名称无法保存')
        else:
            suc = 1
            print('结果:空名称可以保存！错误！')
            return suc
        print('2.输入名称上限（包含数字、英文、中文）')
        if text.startswith('ZigBee'):
            self.input(self.findIpt(self.edit), 'ZigBee '+second_edit)
        else:
            self.input(self.findIpt(self.edit), second_edit)
        text = self.getText_element(self.findIpt(self.edit))
        self.scene_name_list.append(text)
        print('编辑后的新名称为【%s】'%text)
        self.id_click(save_name)
        ele = self.wait_for_element(name_exit)
        if ele:
            print('结果：名称上限可以保存（中/英/数字）')
        else:
            suc = 1
            print('结果:保存失败')
        return suc

    '''检测定位图标是否正常'''
    def location_is_normal(self):
        self.id_click('ci loc nor')
        suc = 0
        ele = self.wait_for_element(id='面板指示灯闪烁30秒 请留意设备位置')
        ele2 = self.wait_for_element(id='定位失败，当前设备已离线')
        ele3 = self.wait_for_element(id='BUS指示灯闪烁30秒 请留意设备位置')
        if ele:
            print('消息弹出框提示的内容【%s】'% ele.text)
            self.id_click('我知道了')
        elif ele2:
            print('消息弹出框提示的内容【%s】'% ele2.text)
            self.id_click('我知道了')
        elif ele3:
            print('消息弹出框提示的内容【%s】'% ele3.text)
            self.id_click('我知道了')
        else:
            suc = 1
            print('定位图标点击无效')
        return suc

    # 当前选选定房间名称--物理设备
    floor_name = []
    def selected_room_name(self, location_type, floorname_eles):
        eles = self.findIpts(location_type)
        location_text = self.getText_element(eles[1])
        if location_text.startswith('设备位置: '):
            name2 = location_text.replace(location_text[0:6], '')
            for i in floorname_eles:
                text = self.element_attribute(i, 'name')
                if text:
                    if text != location_text:
                        if name2.startswith(text):
                            self.floor_name.append(text)
                            break
            c = [i for i in name2 if i not in self.floor_name[-1]]
            selected_name = ''.join(c)
            selected = selected_name.strip()
            return selected
        else:
            for i in floorname_eles:
                text = self.element_attribute(i,'name')
                if text:
                    if text != location_text:
                        if location_text.startswith(text):
                            self.floor_name.append(text)
                            break
            c = [i for i in location_text if i not in self.floor_name[-1]]
            selected_name = ''.join(c)
            selected = selected_name.strip()
            return selected

    # 根据元素长短获取随机数
    def by_eles_for_ran(self, rlist):
        if len(rlist) == 17:
            ran = random.randint(6, 15)
        elif len(rlist) == 18:
            ran = random.randint(7, 16)
        elif len(rlist) == 21:
            ran = random.randint(10, 18)
        elif len(rlist) == 16:
            ran = random.randint(5, len(rlist)-2)
        elif len(rlist) == 15:
            ran = random.randint(7, len(rlist)-2)
        elif len(rlist) == 14:
            ran = random.randint(6, len(rlist)-1)
        elif len(rlist) == 13:
            ran = random.randint(5, len(rlist)-1)
        else:
            ran = random.randint(4, len(rlist)-1)
        return ran


    '''物理设备位置是否正确'''
    default_roomName = []
    def device_location_show_physical(self):
        ele = self.wait_for_element(id='设备位置:')
        self.waitEle_for_up(ele)
        eles = self.findIpts(self.button)
        select_name = self.selected_room_name(self.device_location_physical, eles)
        self.default_roomName.append(select_name)
        print('默认选择的房间为【%s】' % select_name)
        print('---同楼层检测---')
        rlist = self.findIpts(self.roomName)
        ran = self.by_eles_for_ran(rlist)
        self.click_element(rlist[ran])
        room = self.getText_element(rlist[ran])
        print('选择【' + room + '】')
        eles = self.findIpts(self.device_location_physical)
        deviceLocationName = self.getText_element(eles[1])
        print('获取设备位置的文本【%s】' % deviceLocationName)
        print('将获取的文本与楼层房间进行对比')
        suc = 0
        if room in deviceLocationName:
            print('结果：设备位置显示对应选择房间正确')
        else:
            suc = 1
            print('结果：设备位置显示对应选择房间错误')
        return suc

    '''物理设备位置是否正确'''

    def device_location_show2_physical(self):
        self.id_click('2楼')
        print('---不同楼层检测---')
        rlist = self.findIpts(self.roomName)
        self.click_element(rlist[-1])
        room = self.getText_element(rlist[-1])
        print('选择【' + room + '】')
        eles = self.findIpts(self.device_location_physical)
        deviceLocationName = self.getText_element(eles[1])
        print('获取设备位置的文本【%s】' % deviceLocationName)
        print('将获取的文本与楼层房间进行对比')
        suc = 0
        if room in deviceLocationName:
            print('结果：设备位置显示对应选择房间正确')
        else:
            suc = 1
            print('结果：设备位置显示对应选择房间错误')
        return suc

    '''逻辑设备位置是否正确'''

    def device_location_show_logic(self):
        floor_eles = self.findIpts(self.roomName)
        select_name = self.selected_room_name(self.device_location_logic, floor_eles)
        self.default_roomName.append(select_name)
        print('默认选择的房间为【%s】' % select_name)
        print('---同楼层检测---')
        rlist = self.findIpts(self.roomName)
        ran = self.by_eles_for_ran(rlist)
        self.click_element(rlist[ran])
        room = self.getText_element(rlist[ran])
        print('选择【' + room + '】')
        eles = self.findIpts(self.device_location_logic)
        deviceLocationName = self.getText_element(eles[1])
        print('获取设备位置的文本【%s】' % deviceLocationName)
        print('将获取的文本与楼层房间进行拼接对比')
        suc = 0
        if room in deviceLocationName:
            print('结果：设备位置显示对应选择房间正确')
        else:
            suc = 1
            print('结果：设备位置显示对应选择房间错误')
        return suc

    '''逻辑设备位置是否正确'''

    def device_location_show2_logic(self):
        self.id_click('2楼')
        print('---不同楼层检测---')
        rlist = self.findIpts(self.roomName)
        self.click_element(rlist[-1])
        room = self.getText_element(rlist[-1])
        print('选择【' + room + '】')
        eles = self.findIpts(self.device_location_logic)
        deviceLocationName = self.getText_element(eles[1])
        print('获取设备位置的文本【%s】' % deviceLocationName)
        print('将获取的文本与楼层房间进行拼接对比')
        suc = 0
        if room in deviceLocationName:
            print('结果：设备位置显示对应选择房间正确')
        else:
            suc = 1
            print('结果：设备位置显示对应选择房间错误')
        return suc

    '''检验滑动是否正常'''
    def is_swipe(self, name):
        self.id_click(self.floor_name[-1])
        if self.default_roomName[-1].startswith(' '):
            name = self.default_roomName[-1].replace(' ','')
            ele = self.findIpts("name CONTAINS '" + name + "'")
        else:
            ele = self.findIpts("name CONTAINS '" + self.default_roomName[-1] + "'")
        self.click_element(ele[0])
        result = self.waitEle_for_down(name)
        suc = 0
        if result is True:
            print('结果：屏幕滑动正常')
        else:
            suc = 1
            print('结果：屏幕滑动异常')
        return suc

    '''判断是否有接近感应'''
    def is_induction(self):
        ele = self.findIpt("name CONTAINS('指示灯延时关闭')")
        if ele:
            print('有接近感应，进行延时关闭操作')
            eles = self.findIpts(self.roomName)
            self.click_element(eles[9])
            self.swipe_control(122, 368, 272, 368)
            eles = self.findIpts(self.roomName)
            text1 = self.getText_element(eles[1])
            text_first = text1[-3:].replace('s', '秒')
            print('第一次滑动为【%s】' % text_first)
            self.swipe_control(272, 368, 110, 368)
            eles = self.findIpts(self.roomName)
            text2 = self.getText_element(eles[1])
            text_second = text2[-3:].replace('s', '秒').strip()
            print('第二次滑动为【%s】' % text_second)
            self.id_click('确定')
            suc = 0
            if text_second != text_first:
                print('结果：延时关闭调节正常')
            else:
                suc = 1
                print('结果：延时关闭调节异常')
        else:
            suc = 0
            print('无接近感应，跳过延时关闭验证')
        return suc

    '''根据逻辑设备页获取灯位置，进入对应楼层页面'''
    location_text = []
    def enter_room_for_hide_logic(self, location_text):
        eles = self.findIpts(CommonPage.title_roomName)
        self.click_element(eles[-2])
        eles = self.findIpts(self.title_roomName)
        for i in range(2, len(eles)):
            text = self.element_attribute(eles[i], 'name')
            if location_text.startswith(text):
                room = location_text.replace(text, '')
                self.location_text.append(room)
                eles = self.findIpts("name CONTAINS '" + room + "'")
                break
        self.click_element(eles[0])
        ele = self.findIpt(CommonPage.city)
        if not ele:
            CommonPage(self.driver).back()

    '''根据传入对房间名称直接进入对应房间'''
    def enter_room_for_roomName(self, room):
        eles = self.findIpts(CommonPage.title_roomName)
        self.click_element(eles[-2])
        eles = self.findIpts("name CONTAINS '" + room + "'")
        self.click_element(eles[0])
        ele = self.findIpt(CommonPage.city)
        if not ele:
            CommonPage(self.driver).back()

    '''在逻辑设备页获取设备房间楼层信息'''
    def get_location_text(self):
        name_ele = self.findIpts(self.roomName)
        text1 = self.getText_element(name_ele[2])  # 名称
        text2 = self.getText_element(name_ele[3])  # 位置
        return text2, text1

    '''在逻辑设备页获取设备房间楼层信息--对接模块'''
    def get_location_text_ID(self):
        name_ele = self.findIpts(self.roomName)
        text1 = self.getText_element(name_ele[1])  # 名称
        text2 = self.getText_element(name_ele[2])  # 位置
        return text2, text1

    '''回到页面顶部'''
    def back_top(self):
        time.sleep(1)
        ele = self.wait_for_element(id=self.top)
        while ele is None:
            self.swipe_down()
            ele = self.wait_for_element(id=self.top)
        self.swipe_down()


    '''遍历主页的设备名称'''

    def find_deviceName(self, name):
        deviceName = self.findIpt('name CONTAINS("' + name + '")')
        ele1 = self.findIpt('name CONTAINS("传感器")')
        ele2 = self.findIpt('name CONTAINS("其它设备")')
        while not deviceName:
            if ele1 or ele2:
                suc = 0
                print('结果：对比到最后一个了，验证通过')
                break
            self.swipe_up_Big()
            deviceName = self.findIpt('name CONTAINS("' + name + '")')
            ele1 = self.findIpt('name CONTAINS("传感器")')
            ele2 = self.findIpt('name CONTAINS("其它设备")')
        else:
            suc = 1
            print('结果：未隐藏，隐藏功能异常！')
        return suc

    '''保存'''
    def save(self):
        self.id_click('保存')

    '''返回'''
    def back(self):
        self.id_click('返回')

    '''点击家'''
    def home_click(self):
        self.id_click('家')

    '''点击场景'''

    def scene_click(self):
        self.id_click('场景')

    '''用例执行完之后调用此方法，保证回到主页面不影响下个用例执行'''
    def back_home(self):
        home = self.wait_for_element(id='家')
        cancel = self.wait_for_element(id='取消')
        back = self.wait_for_element(id='返回')
        nb_back = self.wait_for_element(id='nb back')
        finish = self.wait_for_element(id='完成')
        while not home:
            while cancel:
                self.click_element(cancel)
                eles = self.findIpts('name CONTAINS("取消")')
                if eles:
                    self.click_element(eles[1])
                home = self.wait_for_element(id='家')
                cancel = self.wait_for_element(id='取消')
                back = self.wait_for_element(id='返回')
                nb_back = self.wait_for_element(id='nb back')
            while back:
                self.click_element(back)
                home = self.wait_for_element(id='家')
                cancel = self.wait_for_element(id='取消')
                back = self.wait_for_element(id='返回')
                nb_back = self.wait_for_element(id='nb back')
            while nb_back:
                self.click_element(nb_back)
                ele = self.wait_for_element(id='确认退出')
                if ele:
                    self.click_element(ele)
                home = self.wait_for_element(id='家')
                cancel = self.wait_for_element(id='取消')
                back = self.wait_for_element(id='返回')
                nb_back = self.wait_for_element(id='nb back')
            while finish:
                self.click_element(finish)
                home = self.wait_for_element(id='家')
                cancel = self.wait_for_element(id='取消')
                back = self.wait_for_element(id='返回')
                nb_back = self.wait_for_element(id='nb back')

        self.click_element(home)
        time.sleep(2)
        eles = self.findIpts(self.title_roomName)
        self.click_element(eles[-2])
        ele = self.wait_for_element(id='住家环境')
        if ele:
            self.back()
            eles = self.findIpts(self.title_roomName)
            self.click_element(eles[-2])
        eles = self.findIpts(self.title)
        self.click_element(eles[1])
        ele = self.findIpt(self.city)
        if not ele:
            self.back()
        self.back_top()

        self.swipe_down()





if __name__ == '__main__':
    # CommonPage(MyDriver.cur_driver()).random_light_logicName()
    str_name = ['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e', 'f', '你', '我', '他', '黑', '豹', '鸽']
    str_sum = []
    for i in range(21):
        a = str_name[random.randint(0, len(str_name) - 1)]
        str_sum.append(a)
    name = ''.join(str_sum)
    print(name)
    print(len(name))