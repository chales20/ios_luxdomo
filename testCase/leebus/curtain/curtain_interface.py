#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 下午2:49
# @Author  : Chenzd
# @Site    : 窗帘主界面编辑
# @File    : curtain_interface.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.leebus.curtain.curtainPage import CurtainPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.curtain.Curtain_interface').getlog()
class Curtain_interface(unittest.TestCase):
    '''窗帘--主界面编辑'''

    @classmethod
    def setUpClass(cls):
        print('窗帘--主界面编辑冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test_curtain_interface(self):
        self.logicName = self.curtainpage.random_curtain_logicName()
        self.commonpage.enter_device_list('窗帘控制面板', self.logicName)
        result = self.curtainpage.curtain_type()
        if result == 1:
            text_list = self.commonpage.get_location_text()
            location = text_list[0]
            name_text = text_list[1]
        else:
            location = self.curtainpage.get_location()
            name_text = '窗帘'
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)

        self.lightpage.random_longPress(name_text)
        self.lightpage.id_click('名称')
        name = self.lightpage.get_logicName()
        print('1. 主界面长按设备名称编辑')
        logger.info('1. 主界面长按设备名称编辑')
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '确定', '完成')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.lightpage.id_click('完成')
        self.lightpage.random_longPress(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        print('2. 主界面长按设备移动到功能检测')
        logger.info('2. 主界面长按设备移动到功能检测')
        result = self.lightpage.move_to(CommonPage.location_text[-1])
        self.assertEqual(0, result, '结果：移动到功能异常')
        print('3. 移动回初始房间')
        logger.info('3. 移动回初始房间')
        self.lightpage.longPress_text(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        self.lightpage.move_to_defaule(CommonPage.location_text[-1])
        time.sleep(1)
        self.commonpage.back_top()
        CommonPage.location_text = []
        CurtainPage.location_text = []
        CommonPage.update_name = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('窗帘--主界面编辑冒烟结束')