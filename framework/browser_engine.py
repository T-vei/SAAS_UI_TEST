#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from SAAS_UI_TEST.framework.logger import Logger
from SAAS_UI_TEST.framework.readconfig import config,TOOL_PATH

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):
    '''
    读取配置文件的浏览器，打开配置指定的页面
    '''

    def __init__(self):
        self.chrome_driver_path = TOOL_PATH + '\\chromedriver.exe'
        self.firfox_driver_path = TOOL_PATH + '\\geckodriver.exe'
        self.edge_driver_path = TOOL_PATH + '\\msedgedriver.exe'

    def open_browser(self):
        browser = config().get('browserType','browserName')
        logger.info('You had open %s browser' % browser)
        url = config().get('testUrl','URL')
        logger.info('You will open the URL %s !!' % url)

        #判断浏览器
        if browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info('Starting Chrome browser.')
        elif browser == 'Firefox':
            driver = webdriver.Firefox(self.firfox_driver_path)
            logger.info('Starting Firefox browser.')
        elif browser == 'IE':
            driver = webdriver.Ie()
            logger.info('Starting IE browser.')
        elif browser == 'Edge':
            driver = webdriver.Edge(self.edge_driver_path)
            logger.info('Starting IE browser.')
        driver.get(url)
        logger.info('Open URL: %s' % url)
        driver.maximize_window()
        logger.info('Maxmize current window')
        #driver.implicitly_wait(10)   #隐式等待10s，如果定位不到元素超过10s就抛出异常
        #logger.info('Set implicitly wait time 10s.')
        print(driver)
        return driver
