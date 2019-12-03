#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 下午3:21
# @Author  : Chenzd
# @Site    : 窗帘逻辑设备
# @File    : curtain_logic.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.commonPage import CommonPage
from page.leebus.light.lightPage import LightPage
from page.leebus.curtain.curtainPage import CurtainPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.curtain.Curtain_logic').getlog()

class Curtain_logic(unittest.TestCase):
    '''窗帘--逻辑设备冒烟'''

    @classmethod
    def setUpClass(cls):
        print('窗帘--逻辑设备冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.commonpage = CommonPage(cls.driver)
        cls.curtainpage = CurtainPage(cls.driver)
        cls.lightpage = LightPage(cls.driver)
        cls.commonpage.back_top()

    def test_curtain_logic(self):
        self.logicName = self.curtainpage.random_curtain_logicName()
        self.commonpage.enter_device_list('窗帘控制面板', self.logicName)
        self.commonpage.get_title()
        print('【%s】' % CommonPage.title_text[-1])
        # 进入逻辑设备
        print('1. 判断是zigbee窗帘还是两线窗帘面板')
        logger.info('1. 判断是zigbee窗帘还是两线窗帘面板')
        result = self.curtainpage.curtain_type_defferent_operation()
        self.assertEqual(0,result,'结果：存在异常')
        print('2. 根据面板类型进行对应操作')
        logger.info('2. 根据面板类型进行对应操作')
        result = self.curtainpage.curtain_operation()
        self.assertEqual(0,result,'结果：存在异常')
        print('3. 如果是刚才是两线窗帘进行隐藏，则现在进行取消隐藏操作,否则执行pass')
        logger.info('3. 如果是刚才是两线窗帘进行隐藏，则现在进行取消隐藏操作,否则执行pass')
        if len(self.curtainpage.hide_text) > 0:
            self.curtainpage.cancle_hide_curtain(CommonPage.title_text[-1])
            print('4. 从主页进入控制页')
            logger.info('4. 从主页进入控制页')
            self.commonpage.enter_room_for_hide_logic(self.curtainpage.location_text[-1])
            self.lightpage.click_device_interface(self.curtainpage.hide_text[-1])
        else:
            print('4. 从主页进入控制页')
            logger.info('4. 从主页进入控制页')
            self.commonpage.enter_room_for_hide_logic(self.curtainpage.location_text[-1])
            self.lightpage.click_device_interface('窗帘')
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
        result = self.commonpage.is_swipe('请设置窗帘开启时长')
        self.assertEqual(0, result, '结果：屏幕滑动异常')
        print('9. 检测设置窗帘时长是否正常')
        logger.info('9. 检测设置窗帘时长是否正常')
        result = self.curtainpage.set_time()
        self.assertEqual(0, result, '结果：设置时长异常')

        self.commonpage.save()
        self.commonpage.back()
        self.commonpage.back_top()
        CommonPage.title_text = []
        self.curtainpage.location_text = []
        self.curtainpage.hide_text = []  # 制空  不影响下次调用


    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('窗帘--逻辑设备冒烟结束')