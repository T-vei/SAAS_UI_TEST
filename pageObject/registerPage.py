#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.pageObject.saasMainPage import saasMainPage

class registerPage(saasMainPage):
    #菜单元素定位
    registerMenu1_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div/div/div/ul/li[3]/ul/li[4]/p'
    registerMenu2_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[3]/ul/li[4]/p'
    currentTapTitle_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/ul[1]/li/p[2]'
    registerFrame_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/div[4]/iframe'
    tabClose_loc = 'xpath >> /html/body/div[1]/div/div/div[1]/ul[1]/li/p[1]/span'

    #页面控件元素定位
    registerBtn_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[15]/button'

    regType0_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[1]/div[2]/p/select'
    regType1_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[1]/div[2]/p/select/option[1]'
    regType2_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[1]/div[2]/p/select/option[2]'

    email_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[3]/div[2]/p/input'
    password_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[5]/div[2]/p/input'
    firstname_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[6]/div[2]/p/input'
    lastname_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[7]/div[2]/p/input'
    selectCountryBtn_loc = 'xpath >> /html/body/div[1]/div/div[3]/div/form/div/div[2]/div/div[10]/div[2]/p/button'
    selectCountryTitle_loc = 'xpath >> /html/body/div[1]/div/div[4]/div/div/div[1]/h4'
    contryListSearch_loc = 'xpath >> /html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[2]/input'
    contryListSearchBtn_loc = 'xpath >> /html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/button'
    countryListSelectIn_loc = 'xpath >> /html/body/div[1]/div/div[4]/div/div/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]/input'



    def registerEamilUser(self,username):
        self.click(self.regType0_loc)  #选择注册类型
        self.click(self.regType1_loc)  #选择邮箱用户
        self.send_keys(self.email_loc,username)  #输入邮箱
        self.send_keys(self.password_loc,'123456')  #输入密码
        self.click(self.selectCountryBtn_loc)
        t = self.get_text(self.selectCountryTitle_loc)
        if t == '选择国家或地区':
            print("选择国家弹窗打开成功！！")
        self.send_keys(self.contryListSearch_loc,'cn')
        self.click(self.contryListSearchBtn_loc)
        self.click(self.countryListSelectIn_loc)



driver = BrowserEngine().open_browser()

page = registerPage(driver)

page.op
page.registerEamilUser("20200724001@a.com")





