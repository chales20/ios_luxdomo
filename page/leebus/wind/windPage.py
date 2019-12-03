#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 下午6:26
# @Author  : Chenzd
# @Site    : 新风页面类
# @File    : windPage.py
# @Software: PyCharm
# @company:  LEELEN
import time
from page.appiumDriver import MyDriver
import filePath
from page.basePage import BasePage
class WindPage(BasePage):

    # 添加面板按钮
    add_panle_btn = '添加面板'

    # 判断是否有添加面板按钮，有则是对接模块0，无则是两线新风1
    def is_add_panle_btn(self):
        ele = self.wait_for_element(id=self.add_panle_btn)
        if ele:
            type_wind = 0
        else:
            type_wind = 1
        return type_wind

    '''
    新风控制页面类####################################################
    '''
    # 新风风速文本
    speed_text = "type=='XCUIElementTypeStaticText'"
    background = "type == 'XCUIElementTypeOther'"
    switch_btn = '开关'
    speed_btn = '风速'
    temperature = '室内温度'

    '''
    新风开启:(4, 193, 125)  # 新风开的颜色
            (173, 182, 181)  # 新风关的颜色
    '''
    def wind_control(self, color):
        open_color = color  # 新风开的颜色
        temp_ele = self.wait_for_element(id=self.temperature)
        suc = 0
        if temp_ele:
            self.id_click(self.switch_btn)
            time.sleep(2)
            eles = self.findIpts(self.background)
            self.del_file(filePath.picture_feedback_path)  # 清除picture_feedback下的所有文件
            self.complete_screen(filePath.screen_path)
            self.icon_screen(filePath.screen_path, filePath.compare_after_path,eles[-3])
            rgba1 = self.get_color(filePath.compare_after_path,100,100)
            if open_color==rgba1:
                print('结果：新风控制成功')
            else:
                suc = 1
                print('结果：新风控制失败')
        else:
            self.id_click(self.switch_btn)
            time.sleep(2)
            eles = self.findIpts(self.background)
            self.del_file(filePath.picture_feedback_path)  # 清除picture_feedback下的所有文件
            self.complete_screen(filePath.screen_path)
            self.icon_screen(filePath.screen_path, filePath.compare_after_path, eles[-1])
            rgba1 = self.get_color(filePath.compare_after_path, 100, 100)
            if open_color == rgba1:
                print('结果：新风控制成功')
            else:
                suc = 1
                print('结果：新风控制失败')
        return suc

    def wind_speed(self):
        eles = self.findIpts(self.speed_text)
        text1 = self.getText_element(eles[-1])
        self.id_click(self.speed_btn)
        time.sleep(3)
        eles = self.findIpts(self.speed_text)
        text2 = self.getText_element(eles[-1])
        suc = 0
        if text1!=text2:
            print('结果：风速控制成功')
        else:
            suc = 1
            print('结果：风速控制失败')
        return suc

if __name__ == '__main__':

    WindPage(MyDriver.cur_driver()).del_file(filePath.picture_feedback_path)  # 清除picture_feedback下的所有文件
    background = "type == 'XCUIElementTypeOther'"
    eles = WindPage(MyDriver.cur_driver()).findIpts(background)
    time.sleep(5)
    WindPage(MyDriver.cur_driver()).complete_screen(filePath.screen_path)
    WindPage(MyDriver.cur_driver()).icon_screen(filePath.screen_path, filePath.compare_after_path, eles[-1])
    rgba1 =WindPage(MyDriver.cur_driver()).get_color(filePath.compare_after_path, 100, 100)
    print(rgba1)