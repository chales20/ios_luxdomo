#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 下午3:04
# @Author  : Chenzd
# @Site    : 智能插座页面类
# @File    : socketPage.py
# @Software: PyCharm
# @company:  LEELEN
import filePath
from page.basePage import BasePage
class SocketPage(BasePage):

    # 开的颜色
    open_color = '(94, 195, 143)'
    # 关的颜色
    close_color = '(178, 179, 181)'

    def click_switch(self):
        self.id_click('开关')

    def check_switch(self, color):
        ele = self.wait_for_element(id='nb back')
        self.del_file(filePath.picture_feedback_path)
        self.complete_screen(filePath.screen_path)
        self.icon_screen(filePath.screen_path, filePath.compare_after_path, ele)
        print('取出控制后的颜色进行对比...')
        rgba = self.get_color(filePath.compare_after_path, 20, 5)
        suc = 0
        if str(rgba) == color:
            print('结果：控制成功')
        else:
            print('结果：控制失败')
            suc = 1
        return suc