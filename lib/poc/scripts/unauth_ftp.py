#!/usr/bin/python
# __author__ = 'jasonsheh'
# -*- coding:utf-8 -*-
from lib.poc.Base import POC
import ftplib


class FtpUnauthorized(POC):
    def __init__(self, ip):
        self.ip = ip

    def info(self):
        info = {
            'name': 'FtpUnauthorized',
            'level': 'high',
            'type': 'unauthorized',
        }
        return info

    def check(self):
        try:
            ftp = ftplib.FTP()
            ftp.connect(self.ip, 21)
            ftp.login()
            ftp.retrlines('LIST')
            ftp.quit()
            return True
        except Exception as e:
            return False


if __name__ == '__main__':
    FtpUnauthorized(ip='115.159.160.21').check()

