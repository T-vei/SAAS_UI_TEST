#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest,ddt
from selenium import webdriver
from SAAS_UI_TEST.pageObject.customer360Page import customer360Page
from SAAS_UI_TEST.pageObject.saasMainPage import saasMainPage
from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.framework.logger import Logger

logger = Logger(logger='TestCase').getlog()

driver = BrowserEngine().open_browser()

page = customer360Page(driver)
page.openPage()
page.searchUser("8619900991745")
page.closePage()
driver.close()
