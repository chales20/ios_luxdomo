#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 下午3:45
# @Author  : Chenzd
# @Site    : 调色灯页面类
# @File    : palettePage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time
import filePath
from page.basePage import BasePage
class palettePage(BasePage):

    # 调色灯图标
    TypeImage = "type=='XCUIElementTypeImage'"
    # 开灯图标
    open_icon = 'rgb_light_on'
    # 关灯图标
    close_icon = 'rgb_light_off'
    # 收藏-空白图标
    collection_icon = 'rgb_add_nor'
    # 百分比
    StaticText = "type=='XCUIElementTypeStaticText'"

    # 调色灯打开
    open_rgba2 = []
    def palette_control(self, icon):
        eles = self.findIpts(self.TypeImage)
        self.click_element(eles[0])
        print('1.控一下开关')
        time.sleep(2)
        eles = self.findIpts(self.TypeImage)
        text = self.element_attribute(eles[0], 'name')
        print('2.获取出图标值进行判断')
        suc = 0
        if text == icon:
            print('结果：控制成功')
        else:
            suc = 1
            print('结果：控制失败')
        self.del_file(filePath.picture_feedback_path)
        self.complete_screen(filePath.screen_path)
        self.icon_screen(filePath.screen_path, filePath.compare_after_path, eles[0])
        print('1.取出控制后的颜色')
        self.open_rgba2.append(self.get_color(filePath.compare_after_path, 100, 100))
        return suc

    # 调整饱和度
    def open_saturationbar(self):
        eles = self.findIpts(self.TypeImage)
        self.swipe_control(303,493,125,493)
        self.del_file(filePath.picture_feedback_path)
        self.complete_screen(filePath.screen_path)
        self.icon_screen(filePath.screen_path, filePath.compare_after_path, eles[0])
        print('1.取出控制后的颜色')
        control_rgba1 = self.get_color(filePath.compare_after_path, 100,100)
        suc = 0
        if self.open_rgba2[-1] != control_rgba1:
            print('结果：调节成功')
        else:
            suc = 1
            print('结果：调节失败')
        self.swipe_control(125, 493, 303, 493)
        return suc

    # 调整亮度
    def control_brighter(self):
        self.swipe_control(300,576,120,576)
        time.sleep(2)
        eles = self.findIpts(self.StaticText)
        text1 = self.getText_element(eles[-1])
        print('1.调整亮度后获取出百分比【%s】'% text1)
        self.swipe_control(120,576,300,576)
        time.sleep(2)
        eles = self.findIpts(self.StaticText)
        text2 = self.getText_element(eles[-1])
        print('2.调整亮度后获取出百分比【%s】' % text2)
        suc = 0
        if text1 != text2:
            print('结果：调节成功')
        else:
            suc = 1
            print('结果：调节失败')
        return suc

    # 检验收藏功能
    ran_just = []
    def check_collection(self):
        eles_first = self.wait_for_elements(id=self.collection_icon)
        ran = random.randint(0, len(eles_first)-1)
        self.ran_just.append(ran)
        self.click_element(eles_first[ran])
        eles_second = self.wait_for_elements(id=self.collection_icon)
        suc = 0
        if len(eles_first) != len(eles_second):
            print('结果：收藏成功')
        else:
            suc = 1
            print('结果：收藏失败')
        return suc

    # 删除收藏的颜色
    def delete_collection(self):
        eles = self.findIpts(self.TypeImage)
        eles_list = [eles[3], eles[5], eles[7], eles[9]]
        self.longPress_palette(eles_list[self.ran_just[-1]])
        eles = self.findIpts(self.StaticText)
        text = self.getText_element(eles[-1])
        print('弹出的内容【%s】' % text)
        self.id_click('是')
        time.sleep(2)
        eles_list = self.wait_for_elements(id=self.collection_icon)
        suc = 0
        if len(eles_list) == 4:
            print('结果：删除成功')
        else:
            suc = 1
            print('结果：删除失败')
        return suc