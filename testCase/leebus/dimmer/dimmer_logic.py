#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/28 上午11:32
# @Author  : Chenzd
# @Site    : 调光灯逻辑设备
# @File    : dimmer_logic.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.dimmer.dimmerPage import DimmerPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.dimmer.Dimmer_logic').getlog()

class Dimmer_logic(unittest.TestCase):
    '''调光--逻辑设备冒烟'''

    @classmethod
    def setUpClass(cls):
        print('调光--逻辑设备冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.dimmerpage = DimmerPage(cls.driver)
        cls.commonpage.back_top()

    def test_dimmer_logic(self):
        self.logicName = '调光灯'
        self.commonpage.enter_device_list_random('调光', self.logicName)
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        # 进入逻辑设备
        print('1. 点击隐藏，判断是否有弹框')
        logger.info('1. 点击隐藏，判断是否有弹框')
        result = self.dimmerpage.dimmer_hide_click()
        self.assertEqual(0,result,'结果：存在异常')
        print('2. 在主页检测是否隐藏成功')
        logger.info('2. 在主页检测是否隐藏成功')
        result = self.dimmerpage.dimmer_hide_normal()
        self.assertEqual(0,result,'结果：存在异常')
        self.commonpage.back_top()
        print('3. 取消隐藏')
        logger.info('3. 取消隐藏')
        self.dimmerpage.cancle_hide_dimmer(CommonPage.physical_device[-1], CommonPage.title_text[-1])
        self.commonpage.swipe_down()
        print('4. 从主页进入控制页')
        logger.info('4. 从主页进入控制页')
        self.lightpage.click_device_interface('调光灯')
        self.commonpage.enter_menu()
        name = self.lightpage.get_logicName()
        print('5. 设备名称编辑')
        logger.info('5. 设备名称编辑')
        result = self.commonpage.edit_name('', name + self.commonpage.random_name(), '保存', '返回')
        self.assertEqual(0, result, '结果：名称编辑异常')
        self.commonpage.enter_menu()
        print('6. 检测定位图标是否正常')
        logger.info('6. 检测定位图标是否正常')
        result = self.commonpage.location_is_normal()
        self.assertEqual(0, result, '结果：图标定位异常')
        print('7. 检测设备位置显示是否正确')
        logger.info('7. 检测设备位置显示是否正确')
        result = self.commonpage.device_location_show_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        result = self.commonpage.device_location_show2_physical()
        self.assertEqual(0, result, '结果：设备位置显示错误')
        print('8. 检测滑动屏幕是否正常')
        logger.info('8. 检测滑动屏幕是否正常')
        result = self.commonpage.is_swipe('楼层房间配置')
        self.assertEqual(0, result, '结果：屏幕滑动异常')

        self.commonpage.save()
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.title_text = []
        CommonPage.physical_device = []


    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('调光--逻辑设备冒烟结束')