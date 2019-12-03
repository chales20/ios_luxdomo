#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 上午9:17
# @Author  : Chenzd
# @Site    : 记录
# @File    : record_edit.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.Cloud.opinion_feedback.feedbackPage import FeedbackPage
from page.leebus.commonPage import CommonPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.opinion_feedback.record_edit').getlog()
class record_edit(unittest.TestCase):
    '''意见反馈--记录编辑冒烟开始'''

    @classmethod
    def setUpClass(cls):
        print('意见反馈--记录编辑冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.feedbackPage = FeedbackPage(cls.driver)
        cls.commonPage = CommonPage(cls.driver)

    def test_record_edit(self):
        self.feedbackPage.enter_feedback()
        self.feedbackPage.click_record()
        print('1. 检测是否有刚提交的记录')
        logger.info('1. 检测是否有刚提交的记录')
        result = self.feedbackPage.check_record()
        self.assertEqual(0, result, '结果：提交记录异常')
        self.feedbackPage.click_edit()
        print('2. 检测全选')
        logger.info('2. 检测全选')
        result = self.feedbackPage.all_chose()
        self.assertEqual(0, result, '结果：全选异常')
        print('3. 检测删除')
        logger.info('3. 检测删除')
        result = self.feedbackPage.check_delete()
        self.assertEqual(0, result, '结果：删除异常')
        self.commonPage.back()
        self.commonPage.id_click('nb back')
        self.commonPage.id_click('确认退出')
        self.commonPage.home_click()

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('意见反馈--记录编辑冒烟结束')