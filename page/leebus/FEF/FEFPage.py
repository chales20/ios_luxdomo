#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 下午2:10
# @Author  : Chenzd
# @Site    : 485页面类
# @File    : FEFPage.py
# @Software: PyCharm
# @company:  LEELEN
import random
import time

import filePath
from page.basePage import BasePage
class FEFPage(BasePage):

    # 空调--------------------------

    # 风速
    low = 'ac low nor'
    mid = 'ac mid nor'
    high = 'ac high nor'

    # 模式
    cold = 'ac cold nor'
    cs = 'ac cs nor'
    hot = 'ac hot nor'
    wind = 'ac wind nor'

    # 打开空调并控制
    def open_condition(self):
        ele = self.wait_for_element(id='开关')
        self.click_element(ele)
        attr = self.element_attribute(ele, 'value')
        suc = 0
        if attr == '1':
            print('结果：打开空调成功')
        else:
            suc = 1
            print('结果：打开空调失败')
        return suc

    # 控制空调
    def control_condition(self):
        time.sleep(2)
        speed = [self.low, self.mid, self.high]
        text1 = ['低速', '中速', '高速']
        module = [self.cold, self.cs, self.hot, self.wind]
        text2 = ['制冷', '除湿', '制热', '送风']
        ran1 = random.randint(0, len(speed)-1)
        ran2 = random.randint(0, len(module)-1)
        suc = 0
        ele = self.wait_for_element(speed[ran1])
        self.click_element(ele)
        time.sleep(2)
        print('控制风速为【%s】' % text1[ran1])
        attr1 = self.element_attribute(ele, 'value')
        if attr1 == '1':
            print('结果：风速控制成功')
        else:
            suc = 1
            print('结果：风速控制失败')
        ele = self.wait_for_element(module[ran2])
        self.click_element(ele)
        time.sleep(2)
        print('控制模式为【%s】' % text2[ran2])
        attr2 = self.element_attribute(ele, 'value')
        if attr2 == '1':
            print('结果：模式控制成功')
        else:
            suc = 1
            print('结果：模式控制成功')
        return suc

    # 关闭空调
    def close_condition(self):
        ele = self.wait_for_element(id='开关')
        self.click_element(ele)
        attr = self.element_attribute(ele, 'value')
        suc = 0
        if attr == '1':
            suc = 1
            print('结果：关闭空调失败')
        else:
            print('结果：关闭空调成功')
        return suc

    # 地暖 --------------------------------------------------------
    '''
    开的颜色:
    '(58, 169, 189)'
    关的颜色:
    '(173, 182, 181)'
    '''
    switch_btn = '开关'
    background = "type == 'XCUIElementTypeOther'"

    def warm_control(self, color):
        open_color = color  # 新风开的颜色
        self.id_click(self.switch_btn)
        time.sleep(2)
        eles = self.findIpts(self.background)
        self.del_file(filePath.picture_feedback_path)  # 清除picture_feedback下的所有文件
        self.complete_screen(filePath.screen_path)
        self.icon_screen(filePath.screen_path, filePath.compare_after_path, eles[-1])
        rgba1 = self.get_color(filePath.compare_after_path, 100, 100)
        suc = 0
        if open_color == rgba1:
            print('结果：地暖控制成功')
        else:
            suc = 1
            print('结果：地暖控制失败')
        return suc