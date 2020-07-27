#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SAAS_UI_TEST.framework.base_page import BasePage
from SAAS_UI_TEST.pageObject.saasLoginPage import saasloginPage
from SAAS_UI_TEST.framework.readconfig import config

class saasMainPage(BasePage):
    # 登录页面元素定位
    user_name_loc = 'xpath >> /html/body/section/div/ul/li[3]/input'
    pass_word_loc = 'xpath >> /html/body/section/div/ul/li[4]/input'
    error_loc = 'xpath >> /html/body/section/div/ul/li[5]/span'
    loginBtn_loc = 'xpath >> /html/body/section/div/ul/li[6]/input'
    account_loc = 'xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[4]/a'
    loginout_loc = "xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[4]/ul/li[2]/a"
    # SaaS开始页面元素定位
    operator_loc = 'xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[3]/a'
    operatorTitle_loc = 'xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[3]/li[3]/a/span[1]'
    orgOperator1_loc = 'link_text >> COMMON - API测试专用一'
    businessDev_loc = 'xpath >> /html/body/div[1]/div/div/div[2]/div[2]/div[1]'
    systemMgmt_loc = 'xpath >> /html/body/div[1]/div/div/div[2]/div[2]/div[2]'
    businessPre_loc = 'xpath >> /html/body/div[1]/div/div/div[2]/div[2]/div[3]'
    operationMat_loc = 'xpath >> /html/body/div[1]/div/div/div[2]/div[2]/div[4]'
    # 服务菜单列表定位
    currentMenuTitle_loc = 'xpath >> /html/body/nav/div[1]/div/div/div[2]/ul[1]/li/a/span[1]'  #检查当前菜单是否是业务开展/系统管理
    customer360_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div/ul/li[3]/ul/li[2]/ul/li/p'


    def saasLogin(self):
        #读取配置文件里的操作员账号登录SaaS
        operUser = config().get('saasOperator','username')
        pwd = config().get('saasOperator','pwd')
        print(self.user_name_loc)
        self.send_keys(self.user_name_loc,operUser)
        self.send_keys(self.pass_word_loc,pwd)
        self.click(self.loginBtn_loc)

    def saasLogout(self):
        self.click(self.account_loc)
        self.click(self.loginout_loc)


    def selectORGOperator(self):
        self.click(self.operator_loc)
        self.click(self.orgOperator1_loc)
        self.wait(1)
        t = self.get_text(self.operatorTitle_loc)
        if t == 'COMMON - API测试专用一':
            print("Select operator {0} success!!".format(t))
        else:
            print("Select operator {0} success!!".format(t))

    def selectSAASOperator(self):
        pass  #选择平台操作员

    def selectMenu1(self):
        '''选择业务开展菜单'''
        self.click(self.businessDev_loc)
        self.wait(1)
        t = self.get_text(self.currentMenuTitle_loc)
        if t == "业务开展":
            print("Select menu {0} success !!".format(t))
        else:
            print("Select menu {0} failed !!".format(t))

    def selectMenu2(self):
        '''选择系统管理菜单'''
        self.click(self.systemMgmt_loc)
        self.wait(1)
        t = self.get_text(self.currentMenuTitle_loc)
        if t == "系统管理":
            print("Select menu {0} success !!".format(t))
        else:
            print("Select menu {0} failed !!".format(t))

    def selectMenu3(self):
        '''选择业务准备菜单'''
        self.click(self.businessPre_loc)
        self.wait(1)
        t = self.get_text(self.currentMenuTitle_loc)
        if t == "业务准备":
            print("Select menu {0} success !!".format(t))
        else:
            print("Select menu {0} failed !!".format(t))

    def selectMenu4(self):
        '''选择运营监管菜单'''
        self.click(self.operationMat_loc)
        self.wait(1)
        t = self.get_text(self.currentMenuTitle_loc)
        if t == "运营监管":
            print("Select menu {0} success !!".format(t))
        else:
            print("Select menu {0} failed !!".format(t))

    def selectServiceMenu(self,loc):
        self.click(loc)

    

