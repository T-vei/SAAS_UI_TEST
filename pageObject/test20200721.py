#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time,unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from SAAS_UI_TEST.framework.logger import Logger
from SAAS_UI_TEST.framework.readconfig import config,TOOL_PATH
from SAAS_UI_TEST.framework.base_page import BasePage
from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.pageObject.saasLoginPage import saasloginPage

logger = Logger(logger='TestCase').getlog()
#driver = webdriver.Chrome(chrome_driver_path)

#driver.get('https://saas2.ukelink.net/')

#time.sleep(5)
#chrome_driver_path = TOOL_PATH + '\\chromedriver.exe'
#driver = webdriver.Chrome(chrome_driver_path)
#url = 'https://saas2.ukelink.net/'

user_name_loc = 'xpath >> /html/body/section/div/ul/li[3]/input'
pass_word_loc = 'xpath >> /html/body/section/div/ul/li[4]/input'
error_loc = 'xpath >> /html/body/section/div/ul/li[5]/span'
button_loc = 'xpath >> /html/body/section/div/ul/li[6]/input'
loginout_loc = "id >> #loginOut"
form_title_loc = 'xpath >> /html/body/section/div/ul/li[1]/text()'
driver = BrowserEngine().open_browser()
loginpage = saasloginPage(driver)


loginpage.type_username('aaaaaaa888')
loginpage.type_password('123456888')
loginpage.click_loginButton()
loginpage.getele()

er2 = loginpage.get_error()
print(type(er2))
if er2 == '用户不存在':
    logger.info("测试通过了！！！！！！")
logger.info(er2)
time.sleep(5)
driver.close()
#page = BasePage(driver)
#er = page.get_text(form_title_loc)
#print("er siss  "+er)


'''
if __name__=='__main__':
    unittest.main()
'''



