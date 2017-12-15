#-*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders, Utils
import smtplib
from email.Header import Header


import getopt, sys
reload(sys)
sys.setdefaultencoding('utf-8')

def SendToKindle(filename):

    filename = filename + ".txt"
    server = 'smtp.163.com'
    username = "rufus_tang"
    password = 'y880228'
    from_mail = 'rufus_tang@163.com'
    to_mail = '15825279415_e6b0cb@kindle.cn'

    smtp = smtplib.SMTP()
    smtp.connect(server)
    smtp.login(username, password)

    msg = MIMEMultipart()
    msg['to'] = to_mail
    msg['from'] = from_mail
    msg['Subject'] = "Convert"
    msg['Date'] = Utils.formatdate(localtime=1)

    content = open(filename, 'rb').read()
    att = MIMEText(content, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att["Content-Disposition"] = "attachment;filename=\"%s\"" % Header(filename, 'gb2312')

    msg.attach(att)

    smtp.sendmail(msg['from'], msg['to'], msg.as_string())
    smtp.quit()



def save2file(filename, content):
    # 保存为电子书文件
    filename = filename + ".txt"
    f = open(filename, 'a')
    f.write(content)
    f.close()



def isElementExist(browser, element):
    flag = True
    try:
        browser.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        return flag

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

    return browser

def get_content(filename,browser_chrome,url):
    # 登录网站
    # browser_chrome = login(browser_chrome)
    time.sleep(2)

    browser_chrome.get(url)

    # 关闭提示框
    if isElementExist(browser_chrome, "//*[@id=\"beginnerGuidePopup_closeBtn\"]"):
        browser_chrome.find_element_by_xpath("//*[@id=\"beginnerGuidePopup_closeBtn\"]").click()
    time.sleep(2)


    i=0

    while True:
        i += 1
        if i>4:
            break

        # 提取标题
        if isElementExist(browser_chrome, "//*[@id=\"chaptercontainer\"]/div/div[1]/h1"):
            title =  "\r\n" + browser_chrome.find_element_by_xpath("//*[@id=\"chaptercontainer\"]/div/div[1]/h1").text

        # 提取内容
        if isElementExist(browser_chrome, "//*[@id=\"chaptercontainer\"]/div/div[2]/div/div"):
            content =  browser_chrome.find_element_by_xpath("//*[@id=\"chaptercontainer\"]/div/div[2]/div/div").text
            content = content.replace("\n","\n\r")
            content = title + "\r\n" + content
            save2file(filename,content)

        # 翻下一页
        if isElementExist(browser_chrome,"//*[@id=\"rightFloatBar_nextChapterBtn\"]"):
            browser_chrome.find_element_by_xpath("//*[@id=\"rightFloatBar_nextChapterBtn\"]").click()
        else:
            break

if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:u:", [])
    except getopt.GetoptError:
        # print help information and exit:
        pass

    for name, value in opts:
            if  name in ("-u"):
                url1 = value
            if name in ("-f"):
                filename1 = value

    filename = filename1
    browser_chrome = webdriver.Chrome()
    url = url1

    get_content(filename, browser_chrome, url)

    # SendToKindle(filename)

    sys.exit()