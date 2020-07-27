#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SAAS_UI_TEST.framework.base_page import BasePage
from SAAS_UI_TEST.pageObject.saasMainPage import saasMainPage


class customer360Page(saasMainPage):
    #菜单元素定位
    customer360L1_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div/ul/li[3]/ul/li[2]/p'
    customer360L2_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[3]/ul/li/p'
    currentTapTitle_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/ul[1]/li/p[2]'
    customer360Frame_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[4]/iframe'
    tabClose_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/ul[1]/li/p[1]/span'   #个人客户管理tap页关闭按钮
    #页面控件元素定位
    searchBtn_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/button'
    search_usrnameInput_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/input[1]'
    userListTd1_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/table/tbody[1]/tr/td[3]/span'
    userListTr_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/table/tbody[1]/tr'

    userListTrSelect_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div/div[1]/table/tbody[1]/tr/td[1]/input[1]'

    userDdetail1_loc = 'xpath >> /html/body/div[1]/div/div[3]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[2]/p'
    #打开个人客户管理菜单页面
    def openPage(self):
        self.saasLogin()
        self.selectMenu1()
        #self.move_to_element(self.customer360L1_loc)
        #self.move_to_element(self.customer360L2_loc)
        self.click(self.customer360L1_loc)
        self.click(self.customer360L2_loc)
        t = self.get_text(self.currentTapTitle_loc)
        if t == '个人客户管理':
            print("Open service menu page {0} success !!".format(t))
        else:
            print("Open service menu page {0} failed !!".format(t))
        self.switch_to_frame(self.customer360Frame_loc)

    def closePage(self):
        self.switch_to_frame_out()
        t = self.get_text(self.currentTapTitle_loc)
        if t == '个人客户管理':
            print("跳出iframe成功！！！ {0} success !!".format(t))
        else:
            print("跳出iframe失败！！！ {0} failed !!".format(t))
        self.click(self.tabClose_loc)
        self.saasLogout()

    def searchUser(self,userCode):
        self.send_keys(self.search_usrnameInput_loc,userCode)
        self.click(self.searchBtn_loc)
        #self.click(self.userListTrSelect_loc)
        tr = self.get_element(self.userListTr_loc)
        print(tr)
        self.click(self.userListTr_loc)
        t = self.get_text(self.userDdetail1_loc)
        if t == userCode:
            print("Search user {0} success !!".format(t))
        else:
            print("Search failed {0} isnot {1} !!".format(t,userCode))