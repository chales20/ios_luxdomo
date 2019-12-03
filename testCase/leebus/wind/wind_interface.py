#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 上午8:49
# @Author  : Chenzd
# @Site    : 新风主界面编辑
# @File    : wind_interface.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.leebus.wind.windPage import WindPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.wind.wind_interface.Wind_interface').getlog()
class Wind_interface(unittest.TestCase):
    '''新风--主界面编辑'''

    @classmethod
    def setUpClass(cls):
        print('新风--主界面编辑冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.windpage = WindPage(cls.driver)
        cls.commonpage.back_top()

    def test_wind_interface(self):
        self.logicName = '新风执行器'
        self.commonpage.enter_device_list_random('新风', self.logicName)
        # 进入逻辑设备
        print('1. 判断是否有添加面板按钮，有则是对接模块0，无则是两线新风1')
        logger.info('1. 判断是否有添加面板按钮，有则是对接模块0，无则是两线新风1')
        result = self.windpage.is_add_panle_btn()
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        if result == 1:
            text_list = self.commonpage.get_location_text()
            location = text_list[0]
            name_text = text_list[1]
        else:
            text_list = self.commonpage.get_location_text_ID()
            location = text_list[0]
            name_text = text_list[1]
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
        print('3. 移动回默认房间')
        self.lightpage.random_longPress(CommonPage.update_name[-1])
        self.lightpage.id_click('移动到')
        self.lightpage.move_to_defaule(CommonPage.location_text[-1])
        time.sleep(1)
        self.commonpage.back_top()

        CommonPage.location_text = []
        CommonPage.update_name = []
        CommonPage.title_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('新风--主界面编辑冒烟结束')