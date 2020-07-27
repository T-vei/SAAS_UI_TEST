#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from SAAS_UI_TEST.framework.readconfig import config,LOG_PATH
import logging
import os.path
from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.framework.logger import Logger
'''
level = logging.DEBUG
logger = logging.getLogger('browserEngine')
logger.setLevel(level)

logfilename = './logs/log.log'
fh = logging.FileHandler(logfilename)
fh.setLevel(level)

sh = logging.StreamHandler(stream=None)
sh.setLevel(level)

fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)

logger.info('hhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

peth1 = os.path.abspath(__file__)
peth2 = os.path.dirname(__file__)
peth3 = os.path.dirname(os.path.abspath('.'))
print(peth1)
print(peth2)
print(peth3)

'''

browser = BrowserEngine().open_browser()
logger = Logger(logger='BrowserEngine').getlog()
logger.info('testssssssssssssss')