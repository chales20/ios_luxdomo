#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/11 下午3:49
# @Author  : Chenzd
# @Site    : 删除联动
# @File    : delete_linkage.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.leebus.linkage.linkagePage import linkagePage
from page.leebus.scene.scenePage import ScenePage
from page.leebus.commonPage import CommonPage
from page.leebus.scene.scene_editPage import Scene_editPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.linkage.delete_linkage').getlog()
class delete_linkage(unittest.TestCase):
    '''删除联动--冒烟'''

    @classmethod
    def setUpClass(cls):
        print('删除联动--冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.scenePage = ScenePage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)
        cls.linkagepage = linkagePage(cls.driver)
        cls.scene_editPage = Scene_editPage(cls.driver)

    def test_delete_linkage(self):
        '''创建快速添加的场景'''
        self.commonPage.scene_click()
        print('1.切换到联动栏并判断是否切换成功')
        logger.info('1.切换到联动栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-1)
        self.assertEqual(0, result, '结果：切换异常')
        while len(self.commonPage.scene_name_list) > 0:
            print('1.=====长按是否有编辑菜单=====')
            logger.info('1.=====长按是否有编辑菜单=====')
            result = self.scene_editPage.enter_sceneEt(self.commonPage.scene_name_list[-1])
            self.assertEqual(0, result, '结果：长按异常')
            self.commonPage.scene_name_list.pop(-1)
            print('2.删除联动')
            logger.info('2.删除联动')
            result = self.linkagepage.delete_linkage()
            self.assertEqual(0, result, '结果：删除异常')
        self.commonPage.swipe_down()
        print('16.切换到场景栏并判断是否切换成功')
        logger.info('16.切换到场景栏并判断是否切换成功')
        result = self.linkagepage.enter_linkage(-2)
        self.assertEqual(0, result, '结果：切换异常')
        self.commonPage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('删除联动--冒烟结束')