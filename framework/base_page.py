#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SAAS_UI_TEST.framework.logger import Logger
from SAAS_UI_TEST.framework.readconfig import config,TOOL_PATH

logger = Logger(logger='BrowserEngine').getlog()
success = 'SUCCESS'
fail = 'FAIL'
class BasePage(object):
    '''
    页面基类，给其他页面继承
    '''
    def __init__(self,driver,base_url=None,title=None):

        self.driver = driver
        self.base_url = base_url
        self.title = title

    def _open(self,url):
        '''
        私有方法，打开url指定页面，并检查页面是否正确
        '''
        self.driver.get(url)
        WebDriverWait(self.driver,10).until(EC.title_is(self.title))#显示等待10s并检查页面标题是否为参数传入的标题

    def open(self):
        '''
        公共方法，打开指定的页面
        '''
        self._open(self.base_url)

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.
        Usage:
        driver.close()
        """
        t1 = time.time()
        self.driver.close()
        logger.info("{0} Closed current window, Spend {1} seconds".format(success, time.time() - t1))

    def quit(self):
        """
        Quit the driver and close all the windows.
        Usage:
        driver.quit()
        """
        t1 = time.time()
        self.driver.quit()
        logger.info("{0} Closed all window and quit the driver, Spend {1} seconds".format(success, time.time() - t1))

    def get_element(self,loc,secs=10):
        by = loc.split(">>")[0].strip()
        value = loc.split(">>")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(loc, secs)
        if by == "id":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.ID, value)), messages)
            element = self.driver.find_element_by_id(value)
            return element
        elif by == "name":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.NAME, value)), messages)
            element = self.driver.find_element_by_name(value)
            return element
        elif by == "class":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)),messages)
            element = self.driver.find_element_by_class_name(value)
            return element
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
            element = self.driver.find_element_by_link_text(value)
            return element
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.XPATH, value)), messages)
            element = self.driver.find_element_by_xpath(value)
            return element
        elif by == "css":
            WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
            element = self.driver.find_element_by_css_selector(value)
            return element
        else:
            raise NameError(
                "Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")

    def max_window(self):
        t1 = time.time()
        self.driver.maximize_window()
        logger.info("{0} Set browser window maximized, Spend {1} seconds".format(success, time.time() - t1))

    def set_window(self, wide, high):
        """
        Set browser window wide and high.
        Usage:
        driver.set_window(wide,high)
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        logger.info("{0} Set browser window wide: {1},high: {2}, Spend {3} seconds".format(success,wide,high,time.time() - t1))

    def send_keys(self, loc, text):
        """
        Operation input box.
        Usage:
        driver.type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            el.send_keys(text)
            logger.info("{0} Typed element: <{1}> content: {2}, Spend {3} seconds".format(success,loc, text,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to type element: <{1}> content: {2}, Spend {3} seconds".format(fail,loc, text,time.time() - t1))
            raise

    def clear_type(self, loc, text):
        """
        Clear and input element.
        Usage:
        driver.clear_type("id->kw","selenium")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            el.clear()
            el.send_keys(text)
            logger.info("{0} Clear and type element: <{1}> content: {2}, Spend {3} seconds".format(success,loc, text,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to clear and type element: <{1}> content: {2}, Spend {3} seconds".format(fail,loc,text,time.time() - t1))
            raise

    def click(self, loc):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..
        Usage:
        driver.click("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            el.click()
            logger.info("{0} Clicked element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def right_click(self, loc):
        """
        Right click element.
        Usage:
        driver.right_click("id >> kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            ActionChains(self.driver).context_click(el).perform()
            logger.info("{0} Right click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to right click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def move_to_element(self, loc):
        """
        Mouse over the element.
        Usage:
        driver.move_to_element("id>>kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("{0} Move to element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} unable move to element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def double_click(self, loc):
        """
        Double click element.
        Usage:
        driver.double_click("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            ActionChains(self.driver).double_click(el).perform()
            logger.info("{0} Double click element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to double click element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def drag_and_drop(self, el_css, ta_css):
        """
        Drags an element a certain distance and then drops it.
        Usage:
        driver.drag_and_drop("id->kw","id->su")
        """
        t1 = time.time()
        try:
            #self.find_element(el_css)
            element = self.get_element(el_css)
            #self.find_element(ta_css)
            target = self.get_element(ta_css)
            ActionChains(driver).drag_and_drop(element, target).perform()
            logger.info("{0} Drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(success,el_css, ta_css,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to drag and drop element: <{1}> to element: <{2}>, Spend {3} seconds".format(fail,el_css,ta_css,time.time() - t1))
            raise

    def click_text(self, text):
        """
        Click the element by the link text
        Usage:
        driver.click_text("新闻")
        """
        t1 = time.time()
        try:
            self.driver.find_element_by_partial_link_text(text).click()
            logger.info("{0} Click by text content: {1}, Spend {2} seconds".format(success, text, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to Click by text content: {1}, Spend {2} seconds".format(fail, text, time.time() - t1))
            raise


    def submit(self, loc):
        """
        Submit the specified form.
        Usage:
        driver.submit("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            el = self.get_element(loc)
            el.submit()
            logger.info("{0} Submit form args element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to submit form args element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def F5(self):
        """
        Refresh the current page.
        Usage:
        driver.F5()
        """
        t1 = time
        self.driver.refresh()
        logger.info("{0} Refresh the current page, Spend {1} seconds".format(success, time.time() - t1))

    def js(self, script):
        """
        Execute JavaScript scripts.
        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        t1 = time.time()
        try:
            self.driver.execute_script(script)
            logger.info("{0} Execute javascript scripts: {1}, Spend {2} seconds".format(success, script, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to execute javascript scripts: {1}, Spend {2} seconds".format(fail,script,time.time() - t1))
            raise

    def get_attribute(self, loc, attribute):
        """
        Gets the value of an element attribute.
        Usage:
        driver.get_attribute("id->su","href")
        """
        t1 = time.time()
        try:
            el = self.get_element(loc)
            attr = el.get_attribute(attribute)
            logger.info("{0} Get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(success,loc, attribute,time.time() - t1))
            return attr
        except Exception:
            logger.info("{0} Unable to get attribute element: <{1}>,attribute: {2}, Spend {3} seconds".format(fail,loc,attribute,time.time() - t1))
            raise

    def get_text(self, loc):
        """
        Get element text information.
        Usage:
        driver.get_text("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            text = self.get_element(loc).text
            logger.info("{0} Get element text element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
            return text
        except Exception:
            logger.info("{0} Unable to get element text element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def get_title(self):
        """
        Get window title.
        Usage:
        driver.get_title()
        """

        t1 = time.time()
        title = self.driver.title
        logger.info("{0} Get current window title, Spend {1} seconds".format(success, time.time() - t1))
        return title

    def get_url(self):
        """
        Get the URL address of the current page.
        Usage:
        driver.get_url()
        """
        t1 = time.time()
        url = self.driver.current_url
        logger.info("{0} Get current window url, Spend {1} seconds".format(success, time.time() - t1))
        return url

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.
        Usage:
        driver.wait(10)
        """
        t1 = time.time()
        self.driver.implicitly_wait(secs)
        logger.info("{0} Set wait all element display in {1} seconds, Spend {2} seconds".format(success,secs,time.time() - t1))

    def accept_alert(self):
        """
        Accept warning box.
        Usage:
        driver.accept_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.accept()
        logger.info("{0} Accept warning box, Spend {1} seconds".format(success, time.time() - t1))

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        Usage:
        driver.dismiss_alert()
        """
        t1 = time.time()
        self.driver.switch_to.alert.dismiss()
        logger.info("{0} Dismisses the alert available, Spend {1} seconds".format(success, time.time() - t1))

    def switch_to_frame(self, loc):
        """
        Switch to the specified frame.
        Usage:
        driver.switch_to_frame("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            iframe_el = self.get_element(loc)
            self.driver.switch_to.frame(iframe_el)
            logger.info("{0} Switch to frame element: <{1}>, Spend {2} seconds".format(success, loc, time.time() - t1))
        except Exception:
            logger.info("{0} Unable switch to frame element: <{1}>, Spend {2} seconds".format(fail, loc, time.time() - t1))
            raise

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        t1 = time.time()
        self.driver.switch_to.default_content()
        logger.info("{0} Switch to frame out, Spend {1} seconds".format(success, time.time() - t1))

    def open_new_window(self, loc):
        """
        Open the new window and switch the handle to the newly opened window.
        Usage:
        driver.open_new_window("id->kw")
        """
        t1 = time.time()
        try:
            original_windows = self.driver.current_window_handle
            el = self.get_element(loc)
            el.click()
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle)
            logger.info("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(success,loc,time.time() - t1))
        except Exception:
            logger.info("{0} Click element: <{1}> open a new window and swich into, Spend {2} seconds".format(fail,loc,time.time() - t1))
            raise

    def element_exist(self, loc):
        """
        judge element is exist,The return result is true or false.
        Usage:
        driver.element_exist("id->kw")
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            logger.info("{0} Element: <{1}> is exist, Spend {2} seconds".format(success, loc, time.time() - t1))
            return True
        except TimeoutException:
            logger.info("{0} Element: <{1}> is not exist, Spend {2} seconds".format(fail, loc, time.time() - t1))
            return False

    def take_screenshot(self, file_path):
        """
        Get the current window screenshot.
        Usage:
        driver.take_screenshot('c:/test.png')
        """
        t1 = time.time()
        try:
            self.driver.get_screenshot_as_file(file_path)
            logger.info("{0} Get the current window screenshot,path: {1}, Spend {2} seconds".format(success,file_path,time.time() - t1))
        except Exception:
            logger.info("{0} Unable to get the current window screenshot,path: {1}, Spend {2} seconds".format(fail,file_path,time.time() - t1))
            raise

    def into_new_window(self):
        """
        Into the new window.
        Usage:
        dirver.into_new_window()
        """
        t1 = time.time()
        try:
            all_handle = self.driver.window_handles
            flag = 0
            while len(all_handle) < 2:
                time.sleep(1)
                all_handle = self.driver.window_handles
                flag += 1
                if flag == 5:
                    break
            self.driver.switch_to.window(all_handle[-1])
            logger.info("{0} Switch to the new window,new window's url: {1}, Spend {2} seconds".format(success,self.driver.current_url,time.time() - t1))
        except Exception:
            logger.info("{0} Unable switch to the new window, Spend {1} seconds".format(fail, time.time() - t1))
            raise

    def type_and_enter(self, loc, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.
        Usage:
        driver.type_css_keys('id->kw','beck')
        """
        t1 = time.time()
        try:
            #self.find_element(loc)
            ele = self.get_element(loc)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
            logger.info("{0} Element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(success, loc, text, secs, time.time() - t1))
        except Exception:
            logger.info("{0} Unable element <{1}> type content: {2},and sleep {3} seconds,input ENTER key, Spend {4} seconds".format(fail, loc, text, secs, time.time() - t1))
            raise

    def js_click(self, loc):
        """
        Input a css selecter,use javascript click element.
        Usage:
        driver.js_click('#buttonid')
        """
        t1 = time.time()
        js_str = "$('{0}').click()".format(loc)
        try:
            self.driver.execute_script(js_str)
            logger.info("{0} Use javascript click element: {1}, Spend {2} seconds".format(success, js_str, time.time() - t1))
        except Exception:
            logger.info("{0} Unable to use javascript click element: {1}, Spend {2} seconds".format(fail,js_str,time.time() - t1))
            raise

    @property
    def origin_driver(self):
        """
        Return the original driver,Can use webdriver API.
        Usage:
        driver.origin_driver
        """
        return self.driver