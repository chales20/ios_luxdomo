#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 下午1:58
# @Author  : Chenzd
# @Site    : 主程序入口
# @File    : runMain.py
# @Software: PyCharm
# @company:  LEELEN
import unittest

import filePath
from public import common
from public.configEmail import Email
from public.readConfig import ReadConfig
from public.configLog import Logger
from runner import HTMLTestRunner

logger = Logger(logger='runMain.RunMain').getlog()

caseList_xls = common.get_excel_case(filePath.testFile_path, 'caseList.xlsx', 'leebus')

class RunMain():
    def __init__(self):
        self.caseFile = filePath.testCase_path
        self.email = Email()
        self.isSend = ReadConfig().get_email('isSend')
        self.caseList = []

    def set_case_list(self):
        for k,v in enumerate(caseList_xls):
            if int(v[3]) == 0:
                self.caseList.append(v[2])
        print(self.caseList)

    def set_case_suit(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.caseList:
            case_name = case.split('/')[-1]
            print(case_name+'.py')
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name+'.py',top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None
        return test_suite

    def run(self):
        filename = filePath.get_filePath(filePath.report_path, '_result.html')
        with open(filename, 'wb') as f:
            try:
                suit = self.set_case_suit()
                if suit is not None:
                    logger.info("----------test start-----------")
                    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'智能家居Luxdomo自动化测试报告', description=u'用例执行情况如下：')
                    runner.run(suit)
                else:
                    logger.info('no case to test')
            except Exception as e:
                logger.error(e)
            finally:
                logger.info("---------- test end -----------")

                if self.isSend == 'on':
                    self.email.send_email(filename)
                elif self.isSend == 'off':
                    logger.info("------ doesn't send result email to. -------")
                else:
                    logger.info("--- unknow state ----")

if __name__ == '__main__':
    RunMain().run()