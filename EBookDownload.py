#-*- coding:utf-8 -*-

import requests
import cookielib
import re
import json
import time
import os
import sys
import os

from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

#全局变量
agent='Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers={'Host':'http://book.qq.com/',
         'Referer':'http://book.qq.com/',
         'User-Agent':agent}

session = requests.session()
session.cookies=cookielib.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except:
    print "Cookie can't load"


def get_xsrf():
    url='http://www.zhihu.com'
    r=session.get(url,headers=headers,allow_redirects=False)
    txt=r.text
    result=re.findall(r'<input type=\"hidden\" name=\"_xsrf\" value=\"(\w+)\"/>',txt)[0]
    return result


def isLogin():
    url='http://dushu.qq.com/read.html?bid=716474&cid=1&sword=%E4%B8%94%E6%8A%8A%E5%B9%B4%E5%8D%8E'
    login_code=session.get(url,headers=headers,allow_redirects=False).status_code
    print login_code
    if login_code == 200:
        return True
    else:
        return False

def main():
    if isLogin():
        print "Has login"
    else:
        print "Need to login"
        # Login()




if __name__ == "__main__":

    sub_folder = os.path.join(os.getcwd(), "content")

    if not os.path.exists(sub_folder):
        os.mkdir(sub_folder)

    os.chdir(sub_folder)

    print os.getcwd()
    get_xsrf()
    # main()

