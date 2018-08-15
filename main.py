import configparser
import os.path
# file check
print("config file checking")
std_id = ""
std_pw = ""
config = configparser.ConfigParser()
if not os.path.isfile("./config.ini"):
    print("config file is not exist.")
    print("what is your Student-id?",end=" ")
    std_id = input()
    print("what is your Password?",end=" ")
    std_pw = input()
    import config_init
    config = config_init.create_ini(std_id,std_pw)
else:
    config.read('config.ini')
    std_id = config['ACCOUNT']['std_id']
    std_pw = config['ACCOUNT']['std_pw']
    print("config file is loaded.")

from selenium import webdriver
from wait_for_response import wait_response
driver = webdriver.Chrome('../chromedriver')
#selenium init
print("[LOGIN] Login Page entry ")
driver.get("https://sugang.suwon.ac.kr/sugang/index.html")
#login site
driver.switch_to_frame(1)
driver.find_element_by_class_name('input_style01').send_keys(std_id)
driver.find_element_by_class_name('input_style02').send_keys(std_pw)
driver.find_element_by_xpath('/html/body/form/div/div/div[1]/div/div[2]/img').click()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# wait = WebDriverWait(driver,300)
import time
from wait_for_response import frame_change
frame_change(driver,2,'menu',0.1)

print("[SUGANG] menu connected")
try:
    driver.switch_to.frame(1)
except:
    pass
wait_response(driver,'class','fldritem',0.1).click()

print("[SUGANG] menu opened")
driver.switch_to.parent_frame()
driver.switch_to.frame(3)
wait_response(driver,'xpath','/html/body/form/table[2]/tbody/tr/td/table/tbody/tr/td/p[1]/span/table/tbody/tr/td/table/tbody/tr/td/p/b/a/font',0.1).click()

print("[SUGANG] SUGANG Page open")
driver.switch_to.window(driver.window_handles[1])
print(driver.page_source)



