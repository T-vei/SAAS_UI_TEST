#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging,datetime,os
from datetime import datetime
from SAAS_UI_TEST.framework.readconfig import config,LOG_PATH

class Logger(object):
    '''
    #日志级别从配置文件读取
    '''
    def __init__(self,logger='Example'):
        #读取日志级别配置
        level = config().get('loggingLevel','level')
        if level == 'DEBUG':
            loggingLevel = logging.DEBUG
        elif level == 'INFO':
            loggingLevel = logging.INFO
        elif level == 'WARNING':
            loggingLevel = logging.WARNING
        elif level == 'ERROR':
            loggingLevel = logging.ERROR
        elif level == 'CRITICAL':
            loggingLevel = logging.CRITICAL
        else:
            print('logging level setting error !!')

        #创建日志文件目录
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)
        logPath = os.path.join(LOG_PATH,str(datetime.now().strftime("%Y-%m-%d")))
        if not os.path.exists(logPath):
            os.mkdir(logPath)

        #设置日志logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(loggingLevel)

        logFile = logPath + '\\log.log'
        fh = logging.FileHandler(logFile)
        fh.setLevel(loggingLevel)

        sh = logging.StreamHandler(stream=None)
        sh.setLevel(loggingLevel)

        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)

        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger

'''
if __name__ == '__main__':
    logger = Logger('BrowserEngine').getlog()
    logger.info('ckfdghjkfghjk')
    
'''