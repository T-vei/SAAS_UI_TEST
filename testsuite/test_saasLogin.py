#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import unittest,ddt
from selenium import webdriver
from SAAS_UI_TEST.pageObject.saasLoginPage import saasloginPage
from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.framework.logger import Logger

logger = Logger(logger='TestCase').getlog()

@ddt.ddt
class test_saasLogin(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserEngine().open_browser()
        self.loginpage = saasloginPage(self.driver)
    def tearDown(self):
        self.driver.close()

    @ddt.data(('abc','123456'),('AT','123456'))
    @ddt.unpack
    def test_saasLogin_1(self,username,password):
        self.loginpage.type_username(username)
        self.loginpage.type_password(password)
        self.loginpage.click_loginButton()
        self.loginpage.get_error()
        logger.info(self.loginpage.get_error())

    @ddt.data(('AT', '123456'))
    @ddt.unpack
    def test_saasLogin_2(self,username,password):
        self.loginpage.type_username(username)
        self.loginpage.type_password(password)
        self.loginpage.click_loginButton()
        time.sleep(3)
        if self.loginpage.isLoginSuccess():
            self.loginpage.click_loginOutButton()
        else:
            print("User is not login status !!")




if __name__=='__main__':
    unittest.main()

