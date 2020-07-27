#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SAAS_UI_TEST.framework.base_page import BasePage

class saasloginPage(BasePage):
    '''
    调用BasePage中的webdriver页面操作方法，将测试页面的用户动作封装
    '''
    #登录页面元素定位
    user_name_loc = 'xpath >> /html/body/section/div/ul/li[3]/input'
    pass_word_loc = 'xpath >> /html/body/section/div/ul/li[4]/input'
    error_loc = 'xpath >> /html/body/section/div/ul/li[5]/span'
    button_loc = 'xpath >> /html/body/section/div/ul/li[6]/input'
    account_loc = 'xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[4]/a'
    loginout_loc = "xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[4]/ul/li[2]/a"

    #页面操作
    def type_username(self,username):
        self.send_keys(self.user_name_loc,username)

    def type_password(self,password):
        self.send_keys(self.pass_word_loc,password)

    def get_error(self):
        err = self.get_text(self.error_loc)
        return err

    def click_loginButton(self):
        self.click(self.button_loc)

    def user_login(self,username,password):
        self.type_username(username)
        self.type_password(password)
        self.click_loginButton()

    def isLoginSuccess(self):
        if self.get_url()=='https://saas82.ukelink.net/saas/index/home':
            return True
        else:
            return False

    def click_loginOutButton(self):
        self.click(self.account_loc)
        self.click(self.loginout_loc)

    def user_loginOut(self):
        try:
            self.get_element(self.error_loc)
        except Exception:
            print('canot get element !!!!!! {0}'.format(self.error_loc))


