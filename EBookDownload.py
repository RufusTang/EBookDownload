#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
import time


from selenium.webdriver.common.action_chains import ActionChains

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def login(browser):
    browser.get('http://book.qq.com')
    time.sleep(2)

    browser.find_element_by_xpath("//*[@id=\"topNav\"]/div/div[2]/div/a[2]").click()
    time.sleep(3)

    browser.switch_to.frame("ui_ywlogin")

    browser.find_element_by_xpath("//*[@id=\"j_loginTab\"]/ul/li[1]").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@id=\"username\"]").send_keys(u"rufus_tang@163.com")
    browser.find_element_by_xpath("// *[ @ id = \"password\"]").send_keys(u"y880228")

    browser.find_element_by_xpath("//*[@id=\"j-inputMode\"]/div[2]/a").click()
    time.sleep(2)

if __name__ == '__main__':

    # try:
    browser_chrome = webdriver.Chrome()

    login(browser_chrome)
    time.sleep(2)


    # except:
    #     print "XXX"