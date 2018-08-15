import time
def wait_response(driver,find_type,args,timer):
    while True:
        try:
            if 'xpath' in find_type:
                return driver.find_element_by_xpath(args)
            elif 'css' in find_type:
                return driver.find_element_by_css_selector(args)
            elif 'name' in find_type:
                return driver.find_element_by_name(args)
            elif 'id' in find_type:
                return driver.find_element_by_id(args)
            elif 'class' in find_type:
                return driver.find_element_by_class_name(args)
            else:
                return None
        except:
            time.sleep(timer)
def frame_change(driver,number,name,timer):
    while True:
        try:
            if name in driver.find_elements_by_xpath('//frame')[number].get_attribute('name'):
                driver.switch_to.frame(driver.find_elements_by_xpath('//frame')[number])

                return number
        except:
            time.sleep(timer)