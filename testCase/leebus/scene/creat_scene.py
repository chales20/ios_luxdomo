#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 上午11:15
# @Author  : Chenzd
# @Site    : 创建场景
# @File    : creat_scene.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.scene.scenePage import ScenePage
from page.leebus.commonPage import CommonPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.scene.creat_scene').getlog()
class creat_scene(unittest.TestCase):
    '''创建场景--冒烟'''

    @classmethod
    def setUpClass(cls):
        print('创建场景--冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.scenePage = ScenePage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)

    def test01_creat_scene(self):
        '''创建快速添加的场景'''
        self.commonPage.scene_click()
        for i in range(1):
            self.scenePage.add_scene()
            self.commonPage.id_click('快速添加设备')
            self.commonPage.id_click('btn add n')
            print('1.添加100个设备后再添加设备')
            logger.info('1.添加100个设备后再添加设备')
            result = self.scenePage.add_advice_by_chose_for()
            self.assertEqual(0, result, '结果：场景添加设备异常')
            self.commonPage.save()
            print('2.随机选择场景图标')
            logger.info('2.随机选择场景图标')
            result = self.scenePage.chonse_item_img()
            self.assertEqual(0, result, '结果：场景图标添加异常')
            print('3.对场景名称进行编辑')
            logger.info('3.对场景名称进行编辑')
            result = self.commonPage.edit_name_scene('',self.commonPage.random_name(),'保存','家')
            self.assertEqual(0, result, '结果：场景名称编辑异常')
            print('4.判断是否创建成功')
            logger.info('4.判断是否创建成功')
            result = self.scenePage.check_creat_custom_scene()
            self.assertEqual(0, result, '结果：场景创建异常')
            print('已创建场景数：【%s】' % str(i+1))
        self.commonPage.swipe_down()
        self.commonPage.home_click()

    def test02_creat_scene(self):
        '''创建自定义场景--包含当前系统的各个类型'''
        self.commonPage.scene_click()
        for i in range(1):
            self.scenePage.add_scene()
            self.scenePage.click_add_device()
            print('1.添加不同类型的设备')
            logger.info('1.添加不同类型的设备')
            self.scenePage.add_device_by_type()
            self.commonPage.save()
            print('2.随机选择场景图标')
            logger.info('2.随机选择场景图标')
            result = self.scenePage.chonse_item_img()
            self.assertEqual(0, result, '结果：场景图标添加异常')
            print('3.对场景名称进行编辑')
            logger.info('3.对场景名称进行编辑')
            result = self.commonPage.edit_name_scene('',self.commonPage.random_name(),'保存','家')
            self.assertEqual(0, result, '结果：场景名称编辑异常')
            print('4.判断是否创建成功')
            logger.info('4.判断是否创建成功')
            result = self.scenePage.check_creat_custom_scene()
            self.assertEqual(0, result, '结果：场景创建异常')
            print('已创建场景数：【%s】' % str(i+1))
        self.commonPage.swipe_down()
        self.commonPage.home_click()



    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('创建场景--冒烟结束')