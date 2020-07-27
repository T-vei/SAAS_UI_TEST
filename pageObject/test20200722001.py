#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from SAAS_UI_TEST.framework.base_page import BasePage
from SAAS_UI_TEST.framework.browser_engine import BrowserEngine
from SAAS_UI_TEST.framework.readconfig import config,TOOL_PATH

form_title_loc = 'xpath >> /html/body/section/div/ul/li[1]'
error_loc = 'xpath >> /html/body/section/div/ul/li[5]/span'
error_loc2 = 'xpath >> /html/body/section/div/ul/li[5]'

user_name_loc = 'xpath >> /html/body/section/div/ul/li[3]/input'
pass_word_loc = 'xpath >> /html/body/section/div/ul/li[4]/input'
button_loc = 'xpath >> /html/body/section/div/ul/li[6]/input'
loginout_loc = "id >> #loginOut"

'''
chrome_driver_path = TOOL_PATH + '\\chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)
url = 'https://saas2.ukelink.net/'
driver.get(url)
'''

driver = BrowserEngine().open_browser()


page = BasePage(driver)

page.send_keys(user_name_loc,'abc')
page.send_keys(pass_word_loc,'123789')
#page.click(button_loc)

time.sleep(5)
er = page.get_text(error_loc)
print("er siss  "+er)

driver.close()