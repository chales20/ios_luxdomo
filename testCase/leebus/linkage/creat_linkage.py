#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/10 上午10:28
# @Author  : Chenzd
# @Site    : 创建联动
# @File    : creat_linkage.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.scene.scenePage import ScenePage
from page.leebus.commonPage import CommonPage
from page.leebus.linkage.linkagePage import linkagePage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.linkage.creat_linkage').getlog()
class creat_linkage(unittest.TestCase):
    '''创建联动--冒烟'''

    @classmethod
    def setUpClass(cls):
        print('创建联动--冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.scenePage = ScenePage(cls.driver)
        cls.linkagepage = linkagePage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)

    def test01_creat_linkage(self):
        '''创建联动--一个房间内所有设备'''
        self.commonPage.scene_click()
        print('1.切换到联动栏并判断是否切换成功')
        logger.info('1.切换到联动栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-1)
        self.assertEqual(0, result, '结果：切换异常')
        for i in range(1):
            self.linkagepage.add_linkage()
            self.commonPage.id_click('btn add n')
            print('1.添加联动条件')
            logger.info('1.添加联动条件')
            self.linkagepage.add_condition()
            result = self.linkagepage.add_condition_next()
            self.assertEqual(0, result, '结果：联动条件异常')
            self.commonPage.save()
            self.linkagepage.add_devices_btn(1)
            self.linkagepage.linkage_device_add()
            self.commonPage.save()
            print('2.添加联动场景')
            logger.info('2.添加联动场景')
            self.linkagepage.click_bottom_btn(1)
            self.linkagepage.add_devices_btn(2)
            self.linkagepage.add_condition()
            self.commonPage.save()
            print('3.编辑联动名称')
            logger.info('3.编辑联动名称')
            result = self.commonPage.edit_name_scene('', self.commonPage.random_name(), '保存', '家')
            self.assertEqual(0, result, '结果：名称编辑异常')
            print('4.判断是否创建成功')
            logger.info('4.判断是否创建成功')
            result = self.scenePage.check_creat_custom_scene()
            self.assertEqual(0, result, '结果：联动创建异常')
            print('已创建联动数：【%s】' % str(i+1))
        self.commonPage.swipe_down()
        print('5.切换到场景栏并判断是否切换成功')
        logger.info('5.切换到场景栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-2)
        self.assertEqual(0, result, '结果：切换异常')
        self.commonPage.home_click()

    def test02_creat_linkage(self):
        '''创建联动--包含当前系统的各个类型'''
        self.commonPage.scene_click()
        print('1.切换到联动栏并判断是否切换成功')
        logger.info('1.切换到联动栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-1)
        self.assertEqual(0, result, '结果：切换异常')
        for i in range(1):
            self.linkagepage.add_linkage()
            self.commonPage.id_click('btn add n')
            print('2.添加联动条件')
            logger.info('2.添加联动条件')
            self.linkagepage.add_condition()
            result = self.linkagepage.add_condition_next()
            self.assertEqual(0, result, '结果：联动条件异常')
            self.commonPage.save()
            self.linkagepage.add_devices_btn(1)
            print('3.添加不同类型的设备')
            logger.info('3.添加不同类型的设备')
            self.scenePage.add_device_by_type()
            self.commonPage.save()
            print('4.添加联动场景')
            logger.info('4.添加联动场景')
            self.linkagepage.click_bottom_btn(1)
            self.linkagepage.add_devices_btn(2)
            self.linkagepage.add_condition()
            self.commonPage.save()
            print('5.编辑联动名称')
            logger.info('5.编辑联动名称')
            result = self.commonPage.edit_name_scene('', self.commonPage.random_name(), '保存', '家')
            self.assertEqual(0, result, '结果：名称编辑异常')
            print('6.判断是否创建成功')
            logger.info('6.判断是否创建成功')
            result = self.scenePage.check_creat_custom_scene()
            self.assertEqual(0, result, '结果：联动创建异常')
            print('已创建联动数：【%s】' % str(i + 1))
        self.commonPage.swipe_down()
        print('7.切换到场景栏并判断是否切换成功')
        logger.info('7.切换到场景栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-2)
        self.assertEqual(0, result, '结果：切换异常')
        self.commonPage.home_click()



    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('创建联动--冒烟结束')