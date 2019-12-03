#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 下午3:52
# @Author  : Chenzd
# @Site    : 意见反馈--问题
# @File    : feedback_edit.py
# @Software: PyCharm
# @company:  LEELEN
import unittest
from page.appiumDriver import MyDriver
from page.Cloud.opinion_feedback.feedbackPage import FeedbackPage
from page.leebus.commonPage import CommonPage
from public.readConfig import Logger
logger = Logger(logger='testCase.leebus.opinion_feedback.feedback_edit').getlog()
class feedback_edit(unittest.TestCase):
    '''意见反馈--问题编辑冒烟开始'''

    @classmethod
    def setUpClass(cls):
        print('意见反馈--问题编辑冒烟开始')
        cls.driver = MyDriver.cur_driver()
        cls.feedbackPage = FeedbackPage(cls.driver)

    def test_feedback_edit(self):
        self.feedbackPage.enter_feedback()
        print('1. 检测默认选择选项')
        logger.info('1. 检测默认选择选项')
        result = self.feedbackPage.check_defaul()
        self.assertEqual(0, result, '结果：默认选中异常')
        print('2. 检测编辑框')
        logger.info('2. 检测编辑框')
        result = self.feedbackPage.edit_suggestEt()
        self.assertEqual(0, result, '结果：编辑框异常')
        print('3. 检测选择问题设备')
        logger.info('3. 检测选择问题设备')
        result = self.feedbackPage.chose_device()
        self.assertEqual(0, result, '结果：选择问题设备异常')
        print('4. 检测添加照片')
        logger.info('4. 检测添加照片')
        result = self.feedbackPage.add_photo()
        self.assertEqual(0, result, '结果：添加照片异常')
        print('5. 检测删除照片')
        logger.info('5. 检测删除照片')
        result = self.feedbackPage.del_photo()
        self.assertEqual(0, result, '结果：添加照片异常')
        print('6. 检测提交')
        logger.info('6. 检测提交')
        result = self.feedbackPage.check_submit()
        self.assertEqual(0, result, '结果：提交异常')

    @classmethod
    def tearDownClass(cls):
        CommonPage(MyDriver.cur_driver()).back_home()
        print('意见反馈--问题编辑冒烟结束')