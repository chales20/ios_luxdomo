#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 上午10:23
# @Author  : Chenzd
# @Site    : 配置邮件
# @File    : configEmail.py
# @Software: PyCharm
# @company:  LEELEN
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import filePath
from public.readConfig import ReadConfig
class Email():
    def __init__(self):
        self.readConfig = ReadConfig()
        global host_ip, host_port, mail_user, mail_passwd, send_user
        host_ip = self.readConfig.get_email('host')
        host_port = self.readConfig.get_email('port')
        mail_user = self.readConfig.get_email('mail_user')
        mail_passwd = self.readConfig.get_email('mail_passwd')
        send_user = self.readConfig.get_email('send_user')

        self.receiver = self.readConfig.get_email('rec_users')
        self.rec_users = []
        for i in str(self.receiver).split(","):
            self.rec_users.append(i)

        # defind email subject
        self.subject = '智能家居APP自动化测试报告'+''+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        self.msg = MIMEMultipart('related')

    # 配置邮件头部
    def config_header(self):
        self.msg['Subject'] = self.subject
        self.msg['Form'] = send_user
        self.msg['To'] = ";".join(self.rec_users)

    # 配置邮件正文
    def config_content(self):
        with open(filePath.emailContent_path, 'r', encoding='utf-8') as f:
            content = f.read()
        content_plain = MIMEText(content, 'html', 'UTF-8')
        self.msg.attach(content_plain)

    # 配置邮件附件
    def config_file(self, reportfile):
        reportfile_name = os.path.basename(reportfile)
        att = MIMEText(open(reportfile, 'rb').read(), 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-steam'
        att['Content-Disposition'] = 'attachment; filename = '+reportfile_name+''
        self.msg.attach(att)

    def send_email(self, reportfile):
        self.config_header()
        self.config_content()
        self.config_file(reportfile)
        try:
            smtp = smtplib.SMTP_SSL(host_ip, host_port)
        except:
            smtp = smtplib.SMTP()
            smtp.connect(host_ip, host_port)

        smtp.login(mail_user, mail_passwd)
        smtp.sendmail(send_user, self.rec_users, self.msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    # print(filePath.report_path)
    email = Email()