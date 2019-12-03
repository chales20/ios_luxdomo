#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 上午11:11
# @Author  : Chenzd
# @Site    : log输出配置
# @File    : configLog.py
# @Software: PyCharm
# @company:  LEELEN
import logging

import filePath


class Logger:

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 写入日志文件
        log_name = filePath.get_filePath(filePath.log_path, '.log')
        fh = logging.FileHandler(log_name,encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)

        # 定义handler到输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

    def getlog(self):
        return self.logger