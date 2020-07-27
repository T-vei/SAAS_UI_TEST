def find_element(self, *loc, secs=5):
    '''
    寻找页面元素
    :param loc: (By.ID,'elementId')
    :param time: timeout
    :return: None

    # 显式等待元素，超过10秒未找到则抛出超时异常(TimeoutException)
    # presence_of_element_located： 不关心元素是否可见，只关心元素是否存在在页面中
    # visibility_of_element_located： 不仅找到元素，并且该元素必须可见
    '''
    loc = str(loc)
    by = loc.split(">>")[0].strip()
    value = loc.split(">>")[1].strip()
    messages = 'Element: {0} not found in {1} seconds.'.format(loc, secs)
    if by == "id":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.ID, value)), messages)
    elif by == "name":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.NAME, value)), messages)
    elif by == "class":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
    elif by == "link_text":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
    elif by == "xpath":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.XPATH, value)), messages)
    elif by == "css":
        WebDriverWait(self.driver, secs, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
    else:
        raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")


def get_element(self, *loc):
    '''
    获取页面元素
    driver.get_element(loc)
    loc:('BY.ID >> elementID')  --string
    '''
    loc = str(loc)
    by = loc.split(">>")[0].strip()
    value = loc.split(">>")[1].strip()
    if by == "id":
        element = self.driver.find_element_by_id(value)
    elif by == "name":
        element = self.driver.find_element_by_name(value)
    elif by == "class":
        element = self.driver.find_element_by_class_name(value)
    elif by == "link_text":
        element = self.driver.find_element_by_link_text(value)
    elif by == "xpath":
        element = self.driver.find_element_by_xpath(value)
    elif by == "css":
        element = self.driver.find_element_by_css_selector(value)
    else:
        raise NameError(
            "Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")
    return element

#检查元素且找到元素
def getwait_element(driver,loc,secs=10):
    by = loc.split(">>")[0].strip()
    value = loc.split(">>")[1].strip()
    messages = 'Element: {0} not found in {1} seconds.'.format(loc, secs)
    print(by)
    print(value)
    if by == "id":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.ID, value)), messages)
        element = driver.find_element_by_id(value)
        return element
    elif by == "name":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.NAME, value)), messages)
        element = driver.find_element_by_name(value)
        return element
    elif by == "class":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, value)), messages)
        element = driver.find_element_by_class_name(value)
        return element
    elif by == "link_text":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.LINK_TEXT, value)), messages)
        element = driver.find_element_by_link_text(value)
        return element
    elif by == "xpath":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.XPATH, value)), messages)
        element = driver.find_element_by_xpath(value)
        return element
    elif by == "css":
        WebDriverWait(driver, secs, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
        element = driver.find_element_by_css_selector(value)
        return element
    else:
        raise NameError(
            "Please enter the correct targeting elements,'id','name','class','link_text','xpaht','css'.")