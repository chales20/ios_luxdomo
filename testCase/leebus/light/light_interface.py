#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 下午4:43
# @Author  : Chenzd
# @Site    : 灯--主界面编辑
# @File    : light_interface.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.light.Light_interface').getlog()
class Light_interface(unittest.TestCase):
    '''灯--主界面编辑'''
    @classmethod
    def setUpClass(cls):
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        print('灯--主界面编辑冒烟开始')
        cls.commonpage.back_top()

    def test_light_interface(self):
        self.lightpage.enter_room_for_hide(CommonPage.default_roomName[-1])
        self.lightpage.random_longPress_light('灯')
        self.lightpage.id_click('名称')
        name = self.lightpage.get_logicName()
        print('1. 主界面长按设备名称编辑')
        logger.info('1. 主界面长按设备名称编辑')
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(),'确定', '完成')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.lightpage.id_click('完成')
        self.lightpage.random_longPress(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        print('2. 主界面长按设备移动到功能检测')
        logger.info('2. 主界面长按设备移动到功能检测')
        result = self.lightpage.move_to(CommonPage.default_roomName[-1])
        self.assertEqual(0,result,'结果：移动到功能异常')
        print('3. 移动回默认房间')
        self.lightpage.longPress_text(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        self.lightpage.move_to_defaule(CommonPage.default_roomName[-1])
        self.commonpage.back_top()

        CommonPage.update_name = []




    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('灯--主界面编辑冒烟结束')