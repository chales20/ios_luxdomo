#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 上午10:19
# @Author  : Chenzd
# @Site    : 读取配置文件
# @File    : readConfig.py
# @Software: PyCharm
# @company:  LEELEN
import configparser
import os
import filePath
from public.configLog import Logger
logger = Logger(logger='public.readConfig.ReadConfig').getlog()

config_file = os.path.join(filePath.config_path, 'config.ini')

class ReadConfig:

    def __init__(self):
        self.configParser = configparser.ConfigParser()
        self.configParser.read(config_file)

    def get_email(self,name):
        value = self.configParser.get('email',name)
        logger.info('读取config.ini文件 email:[%s:%s]'%(name, value))
        return value

if __name__ == '__main__':
    a = ReadConfig().get_email('mail_user')
    print(a)