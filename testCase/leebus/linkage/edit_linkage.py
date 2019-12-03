#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 下午4:40
# @Author  : Chenzd
# @Site    : 联动编辑页
# @File    : edit_linkage.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.scene.scenePage import ScenePage
from page.leebus.scene.scene_editPage import Scene_editPage
from page.leebus.commonPage import CommonPage
from page.leebus.linkage.linkagePage import linkagePage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.linkage.edit_linkage').getlog()
class edit_linkage(unittest.TestCase):
    '''编辑联动--冒烟'''
    @classmethod
    def setUpClass(cls):
        print('编辑联动--冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.scenePage = ScenePage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)
        cls.linkagepage = linkagePage(cls.driver)
        cls.scene_editPage = Scene_editPage(cls.driver)

    def test_edit_linkage(self):
        self.commonPage.scene_click()
        print('1.切换到联动栏并判断是否切换成功')
        logger.info('1.切换到联动栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-1)
        self.assertEqual(0, result, '结果：切换异常')
        print('1.=====长按是否有编辑菜单=====')
        logger.info('1.=====长按是否有编辑菜单=====')
        result = self.scene_editPage.enter_sceneEt(self.commonPage.scene_name_list[-1])
        self.assertEqual(0, result, '结果：长按异常')
        self.linkagepage.click_bottom_btn(0)
        print('2.=====联动中--灯编辑冒烟=====')
        logger.info('2.=====联动中--灯编辑冒烟=====')
        res = self.scene_editPage.each_for('灯')
        if res == 1:
            self.scene_editPage.light_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.action[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('3.=====联动中--窗帘编辑冒烟=====')
        logger.info('3.=====联动中--窗帘编辑冒烟=====')
        res = self.scene_editPage.each_for('窗帘')
        if res == 1:
            device_type = self.scene_editPage.leebus_or_zigbee('位置')
            if device_type == 0:
                self.scene_editPage.curtains_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
                self.assertEqual(0, result, '结果：配置异常')
            if device_type == 1:
                self.scene_editPage.zigbee_curtain_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
                self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('4.=====联动中--新风编辑冒烟=====')
        logger.info('4.=====联动中--新风编辑冒烟=====')
        res = self.scene_editPage.each_for('新风')
        if res == 1:
            self.scene_editPage.curtains_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('5.=====联动中--调光灯编辑冒烟=====')
        logger.info('5.=====联动中--调光灯编辑冒烟=====')
        res = self.scene_editPage.each_for('调光灯')
        if res == 1:
            self.scene_editPage.dimmer_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.dimmer_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('6.=====联动中--中央空调编辑冒烟=====')
        logger.info('6.=====联动中--中央空调编辑冒烟=====')
        res = self.scene_editPage.each_for('中央空调')
        if res == 1:
            self.scene_editPage.aircondition_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.aircondition_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('7.=====联动中--地暖编辑冒烟=====')
        logger.info('7.=====联动中--地暖编辑冒烟=====')
        res = self.scene_editPage.each_for('地暖')
        if res == 1:
            self.scene_editPage.warm_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.warm_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('8.=====联动中--调色灯编辑冒烟=====')
        logger.info('8.=====联动中--调色灯编辑冒烟=====')
        res = self.scene_editPage.each_for('调色灯')
        if res == 1:
            self.scene_editPage.palette_type_linkage()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.palette_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('9.=====联动中--双路通用编辑冒烟=====')
        logger.info('9.=====联动中--双路通用编辑冒烟=====')
        res = self.scene_editPage.each_for('双路通用')
        if res == 1:
            self.scene_editPage.curtains_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('10.=====联动中--机械手编辑冒烟=====')
        logger.info('10.=====联动中--机械手编辑冒烟=====')
        res = self.scene_editPage.each_for('机械手')
        if res == 1:
            self.scene_editPage.curtains_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('11.=====联动中--单路通用编辑冒烟=====')
        logger.info('11.=====联动中--单路通用辑冒烟=====')
        res = self.scene_editPage.each_for('单路通用')
        if res == 1:
            self.scene_editPage.curtains_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('12.=====联动中--声光报警器编辑冒烟=====')
        logger.info('12.=====联动中--声光报警器编辑冒烟=====')
        res = self.scene_editPage.each_for('声光报警器')
        if res == 1:
            device_type = self.scene_editPage.leebus_or_zigbee('ci tick nor')
            if device_type == 0:
                self.scene_editPage.light_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.action[-1])
                self.assertEqual(0, result, '结果：配置异常')
            if device_type == 1:
                self.scene_editPage.curtains_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
                self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('13.=====联动中--电磁阀编辑冒烟=====')
        logger.info('13.=====联动中--电磁阀编辑冒烟=====')
        res = self.scene_editPage.each_for('电磁阀')
        if res == 1:
            device_type = self.scene_editPage.leebus_or_zigbee('ci tick nor')
            if device_type == 0:
                self.scene_editPage.light_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.action[-1])
                self.assertEqual(0, result, '结果：配置异常')
            if device_type == 1:
                self.scene_editPage.curtains_type()
                self.commonPage.save()
                result = self.scene_editPage.contrast_set(self.scene_editPage.curtains_text[-1])
                self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('14.=====联动中--推窗器编辑冒烟=====')
        logger.info('14.=====联动中--推窗器编辑冒烟=====')
        res = self.scene_editPage.each_for('推窗器')
        if res == 1:
            self.scene_editPage.socket_type()
            self.commonPage.save()
            result = self.scene_editPage.contrast_set(self.scene_editPage.socket_text[-1])
            self.assertEqual(0, result, '结果：配置异常')
        self.scene_editPage.back_top()
        print('15.=====联动中--随机删除设备--进入二级界面删除=====')
        logger.info('15.=====联动中--随机删除设备--进入二级界面删除=====')
        result = self.scene_editPage.delete_device()
        self.assertEqual(0, result, '结果：删除异常')
        self.commonPage.save()
        print('16.切换到场景栏并判断是否切换成功')
        logger.info('16.切换到场景栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-2)
        self.assertEqual(0, result, '结果：切换异常')
        self.commonPage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('编辑联动--冒烟结束')