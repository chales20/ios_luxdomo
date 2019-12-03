#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 下午3:02
# @Author  : Chenzd
# @Site    : 智能插座--控制
# @File    : socket_control.py
# @Software: PyCharm
# @company:  LEELEN
import time
import unittest
from page.appiumDriver import MyDriver
from page.leebus.light.lightPage import LightPage
from page.leebus.commonPage import CommonPage
from page.leebus.socket.socketPage import SocketPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.socket.socket_control').getlog()
class socket_control(unittest.TestCase):
    '''智能插座--主界面控制'''

    @classmethod
    def setUpClass(cls):
        print('智能插座--主界面控制冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.socketpage= SocketPage(cls.driver)
        cls.commonpage.back_top()

    def test_socket_control(self):
        self.commonpage.enter_device_list_nextPage('智能墙面插座', '智能墙面插座8')
        text_list = self.commonpage.get_location_text_ID()
        location = text_list[0]
        name_text = text_list[1]
        self.commonpage.back()
        self.commonpage.back()
        self.commonpage.home_click()
        self.commonpage.enter_room_for_hide_logic(location)
        self.lightpage.click_device_interface(name_text)
        print('1. 控制开并检验是否开启成功')
        logger.info('1. 控制开并检验是否开启成功')
        self.socketpage.click_switch()
        result = self.socketpage.check_switch(self.socketpage.open_color)
        self.assertEqual(0, result, '结果：打开异常')
        time.sleep(1)
        print('2. 控制关并检验是否关闭成功')
        logger.info('2. 控制关并检验是否关闭成功')
        self.socketpage.click_switch()
        result = self.socketpage.check_switch(self.socketpage.close_color)
        self.assertEqual(0, result, '结果：关闭异常')
        self.commonpage.id_click('nb back')
        self.commonpage.back_top()
        CommonPage.location_text = []

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('智能插座--主界面控制冒烟结束')
