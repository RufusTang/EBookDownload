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



def cabinet(window_handle):
    # 勾选radio按钮
    # window_handle.find
    # head > th:nth-child(2) > input[type="checkbox"]
    window_handle.find_element_by_xpath("// *[ @ id = \"head\"] / th[2] / input[@ name =\"allbuy\"]").click()

    # 点击“合并采购”
    window_handle.find_element_by_xpath("//*[@id=\"forPage\"]/table[1]/tbody/*/td/input[@value =\"合并发起采购\"]").click()
    time.sleep(2)

    # 处理弹出对话框
    try:
        window_handle.switch_to_alert().accept()
    except:
        pass

    # 对下拉选址框进行操作
    s1 = Select(window_handle.find_element_by_xpath("//*[@id=\"libraryStatus\"]"))
    s1.select_by_index(1)  # 选择第二项选项
    time.sleep(2)

    # 点击立即采购
    window_handle.find_element_by_xpath("// *[ @ id = \"abc\"] / input").click()

    time.sleep(3)

    # 处理弹出对话框
    try:
        window_handle.switch_to_alert().accept()
    except:
        pass

    time.sleep(2)
    # 选择采购部门
    s1 = Select(window_handle.find_element_by_xpath("// *[ @ id =\"costunit\"]"))
    s1.select_by_index(4)  # 选择第二项选项

    time.sleep(2)

    # 选择商品用途
    flag_usage = True
    count_tree = 1
    while flag_usage:
        # try:

        basic_node = "/html/body/div[3]/div[3]/div[2]/table[1]/tbody/tr[" + str(count_tree + 1) + "]/"

        # 树状图的图标
        search_str = basic_node + \
                     "td[4]/input[3]"
        window_handle.find_element_by_xpath(search_str).click()

        time.sleep(2)

        # 双击展开下拉菜单
        search_str = "/html/body/div[3]/div[3]/div[2]/table[1]/tbody/tr[2]/" + \
                     "td[4]/input[3]/" + \
                     "../div/div/div[3]/div/div/ul/li/ul/li/div/a/span"
        print search_str
        DoubleClick1 = window_handle.find_element_by_xpath(search_str)
        ActionChains(window_handle).double_click(DoubleClick1).perform()

        # 选择类型
        time.sleep(2)
        count_element = 1
        while True:

            search_str = "/html/body/div[3]/div[3]/div[2]/table[1]/tbody/tr[2]/" + \
                         "td[4]/input[3]/" + \
                         "../div/div/div[3]/div/div/ul/li/ul/li/ul/li[" + str(count_element) + "]/div/a/span"
            if str(window_handle.find_element_by_xpath(search_str).text) == "经营类资本性开支-主设备":
                time.sleep(2)
                DoubleClick1 = window_handle.find_element_by_xpath(search_str)
                ActionChains(window_handle).double_click(DoubleClick1).perform()
                break
            count_element += 1
            # 如果超过记录数超过15仍未找到，跳出循环
            if count_element > 15:
                break

        # 开始下一个条目的循环，填写下一行记录
        count_tree = count_tree + 1

        # 如果找不到下一个条目，则终止循环
        try:
            basic_node = "/html/body/div[3]/div[3]/div[2]/table[1]/tbody/tr[" + str(count_tree + 1) + "]"

            # 树状图的图标
            search_str = basic_node + "/td[4]/input[3]"
            window_handle.find_element_by_xpath(search_str).click()
        except:
            flag_usage = False

    # 点击合并采购
    time.sleep(2)
    search_str = "/html/body/div[3]/div[3]/div[2]/table[3]/tbody/tr/td[5]/a/img"
    window_handle.find_element_by_xpath(search_str).click()

    time.sleep(2)
    # 点击  确认无误，提交订单
    search_str = "btnSubmit"
    print search_str
    window_handle.find_element_by_id('btnSubmit').click()


    time.sleep(2)
    # 点击 通知发货
    search_str = "/html/body/div[3]/div[3]/div/table[1]/tbody/tr/td[5]/form/input[7]"
    window_handle.find_element_by_xpath(search_str).click()




def design(window_handle):
    # 勾选radio按钮
    # window_handle.find
    # head > th:nth-child(2) > input[type="checkbox"]
    window_handle.find_element_by_xpath("// *[ @ id = \"head\"] / th[2] / input[@ name =\"allbuy\"]").click()

    # 点击“合并采购”
    window_handle.find_element_by_xpath("//*[@id=\"forPage\"]/table[1]/tbody/*/td/input[@value =\"合并发起采购\"]").click()
    time.sleep(2)

    # 处理弹出对话框
    try:
        window_handle.switch_to_alert().accept()
    except:
        pass

    # 对下拉选址框进行操作
    s1 = Select(window_handle.find_element_by_xpath("//*[@id=\"libraryStatus\"]"))
    s1.select_by_index(1)  # 选择第二项选项
    time.sleep(2)

    # 点击立即采购
    window_handle.find_element_by_xpath("//input[@value=\"立即采购\"]").click()

    time.sleep(3)

    # 处理弹出对话框
    try:
        window_handle.switch_to_alert().accept()
    except:
        pass

    # 选择采购部门
    s1 = Select(window_handle.find_element_by_xpath("// *[ @ id =\"costunit\"]"))
    s1.select_by_index(4)  # 选择第二项选项

    time.sleep(2)



    # 点击合并采购
    time.sleep(2)
    search_str = "/html/body/div[3]/div[3]/div[2]/table[3]/tbody/tr/td[5]/a/img"
    window_handle.find_element_by_xpath(search_str).click()

    time.sleep(2)
    # 点击  确认无误，提交订单
    search_str = "btnSubmit"
    print search_str
    window_handle.find_element_by_id('btnSubmit').click()


    time.sleep(2)
    # 点击 通知发货
    search_str = "/html/body/div[3]/div[3]/div/table[1]/tbody/tr/td[5]/form/input[7]"
    window_handle.find_element_by_xpath(search_str).click()


def supervision(window_handle):
    # 勾选radio按钮
    # window_handle.find
    # head > th:nth-child(2) > input[type="checkbox"]
    window_handle.find_element_by_xpath("// *[ @ id = \"head\"] / th[2] / input[@ name =\"allbuy\"]").click()

    # 点击“合并采购”
    window_handle.find_element_by_xpath("//*[@id=\"forPage\"]/table[1]/tbody/*/td/input[@value =\"合并发起采购\"]").click()
    time.sleep(2)

    # 处理弹出对话框
    try:
        window_handle.switch_to_alert().accept()
    except:
        pass

    time.sleep(2)

    # 对下拉选址框进行操作
    s1 = Select(window_handle.find_element_by_xpath("//*[@id=\"libraryStatus\"]"))
    s1.select_by_index(1)  # 选择第二项选项
    time.sleep(2)

    # 点击立即采购
    window_handle.find_element_by_xpath("//input[@value=\"立即采购\"]").click()



    # 处理弹出对话框
    try:
        time.sleep(3)
        window_handle.switch_to_alert().accept()
    except:
        pass

    # 选择采购部门
    s1 = Select(window_handle.find_element_by_xpath("// *[ @ id =\"costunit\"]"))
    s1.select_by_index(4)  # 选择第二项选项

    time.sleep(2)


    # 点击合并采购
    time.sleep(2)
    search_str = "/html/body/div[3]/div[3]/div[2]/table[3]/tbody/tr/td[5]/a/img"
    window_handle.find_element_by_xpath(search_str).click()

    time.sleep(2)
    # 点击  确认无误，提交订单
    search_str = "btnSubmit"
    print search_str
    window_handle.find_element_by_id('btnSubmit').click()


    time.sleep(2)
    # 点击 通知发货
    search_str = "/html/body/div[3]/div[3]/div/table[1]/tbody/tr/td[5]/form/input[7]"
    window_handle.find_element_by_xpath(search_str).click()


def single_pipe_tower(browser_handle, pre_window_handles):
    # 勾选radio按钮
    # browser_handle.find
    # head > th:nth-child(2) > input[type="checkbox"]
    browser_handle.find_element_by_xpath("// *[ @ id = \"head\"] / th[2] / input[@ name =\"allbuy\"]").click()

    # 点击“合并采购”
    browser_handle.find_element_by_xpath("//*[@id=\"forPage\"]/table[1]/tbody/tr/td[12]/a[1]/img").click()
    time.sleep(2)


    browser_handle.find_element_by_xpath(" // *[ @ id = \"goodsBox\"] / ul / li / a / img").click()
    time.sleep(2)

    # 处理新打开的窗口
    handles = browser_handle.window_handles

    # 切换窗口
    for handle in handles:
        if handle not in  pre_window_handles:
            # print handle
            # 切换至新窗口，进入商合代办列表
            browser_handle.switch_to.window(handle)


            # 树状图的图标
            search_str = "//*[@id=\"openUsageTree\"]"
            browser_handle.find_element_by_xpath(search_str).click()
            time.sleep(2)

            # 双击展开下拉菜单
            search_str ="//*[@id=\"usageDiv\"]/div/div[3]/div/div/ul/li/ul/li/div/a/span"
            print search_str
            DoubleClick1 = browser_handle.find_element_by_xpath(search_str)
            ActionChains(browser_handle).double_click(DoubleClick1).perform()

            # 选择类型
            time.sleep(2)
            count_element = 1
            while True:

                search_str = "//*[@id=\"usageDiv\"]/div/div[3]/div/div/ul/li/ul/li/" \
                                "ul/li[" + str(count_element) + "]/div/a/span"
                print search_str
                if str(browser_handle.find_element_by_xpath(search_str).text) == "经营类资本性开支-主设备":
                    DoubleClick1 = browser_handle.find_element_by_xpath(search_str)
                    ActionChains(browser_handle).double_click(DoubleClick1).perform()
                    break
                count_element += 1
                # 如果超过记录数超过15仍未找到，跳出循环
                if count_element > 15:
                    break

            time.sleep(2)


            # 点击 立即购买

            search_str = "buy_now"
            browser_handle.find_element_by_id('buy_now').click()

            time.sleep(2)
            # 点击 去结账

            search_str = "//*/div[@name=\"shopCartDiv\"]/div[2]/table[3]/tbody/tr/td[5]/a"
            browser_handle.find_element_by_xpath(search_str).click()

            time.sleep(2)

            search_str = "//*/div[@id=\"customWeightDiv\"]/div/div[4]/input[1]"
            print search_str
            browser_handle.find_element_by_xpath(search_str).click()

            time.sleep(2)
            # 点击  确认无误，提交订单
            search_str = "btnSubmit"
            browser_handle.find_element_by_id('btnSubmit').click()

            time.sleep(2)
            # 点击 通知发货
            search_str = "/html/body/div[3]/div[3]/div/table[1]/tbody/tr/td[5]/form/input[7]"
            browser_handle.find_element_by_xpath(search_str).click()


            browser_handle.get(
                'http://www.eshop.chinatowercom.cn:8080/eshop/purchase/toPurchaseTask.do?shopCode=jtjcsd&tabFlag=onlinePurchase')

def unstandard_tower(browser_handle, pre_window_handles):
    # 勾选radio按钮
    # browser_handle.find
    # head > th:nth-child(2) > input[type="checkbox"]
    browser_handle.find_element_by_xpath("// *[ @ id = \"head\"] / th[2] / input[@ name =\"allbuy\"]").click()

    # 点击“合并采购”
    browser_handle.find_element_by_xpath("//*[@id=\"forPage\"]/table[1]/tbody/tr/td[12]/a[1]/img").click()
    time.sleep(2)


    browser_handle.find_element_by_xpath(" // *[ @ id = \"goodsBox\"] / ul / li / a / img").click()
    time.sleep(2)

    # 处理新打开的窗口
    handles = browser_handle.window_handles

    # 切换窗口
    for handle in handles:
        if handle not in  pre_window_handles:
            # print handle
            # 切换至新窗口，进入商合代办列表
            browser_handle.switch_to.window(handle)


            # 树状图的图标
            search_str = "//*[@id=\"openUsageTree\"]"
            browser_handle.find_element_by_xpath(search_str).click()
            time.sleep(2)

            # 双击展开下拉菜单
            search_str ="//*[@id=\"usageDiv\"]/div/div[3]/div/div/ul/li/ul/li/div/a/span"
            print search_str
            DoubleClick1 = browser_handle.find_element_by_xpath(search_str)
            ActionChains(browser_handle).double_click(DoubleClick1).perform()

            # 选择类型
            time.sleep(2)
            count_element = 1
            while True:
                search_str = "//*[@id=\"usageDiv\"]/div/div[3]/div/div/ul/li/ul/li/" \
                                "ul/li[" + str(count_element) + "]/div/a/span"
                if str(browser_handle.find_element_by_xpath(search_str).text) == "经营类资本性开支-主设备":
                    DoubleClick1 = browser_handle.find_element_by_xpath(search_str)
                    ActionChains(browser_handle).double_click(DoubleClick1).perform()
                    break
                count_element += 1
                # 如果超过记录数超过15仍未找到，跳出循环
                if count_element > 15:
                    break

            time.sleep(2)


            # 点击 立即购买

            search_str = "buy_now"
            browser_handle.find_element_by_id('buy_now').click()

            time.sleep(2)
            # 点击 去结账

            search_str = "//*/div[@name=\"shopCartDiv\"]/div[2]/table[3]/tbody/tr/td[5]/a"
            browser_handle.find_element_by_xpath(search_str).click()

            time.sleep(2)

            search_str = "//*/div[@id=\"customWeightDiv\"]/div/div[4]/input[1]"
            print search_str
            browser_handle.find_element_by_xpath(search_str).click()

            time.sleep(2)
            # 点击  确认无误，提交订单
            search_str = "btnSubmit"
            browser_handle.find_element_by_id('btnSubmit').click()

            time.sleep(2)
            # 点击 通知发货
            search_str = "/html/body/div[3]/div[3]/div/table[1]/tbody/tr/td[5]/form/input[7]"
            browser_handle.find_element_by_xpath(search_str).click()


            browser_handle.get(
                'http://www.eshop.chinatowercom.cn:8080/eshop/purchase/toPurchaseTask.do?shopCode=jtjcsd&tabFlag=onlinePurchase')

def main(browser):


    browser.get('http://eip.chinatowercom.cn')
    time.sleep(2)

    # 登录
    browser.find_element_by_name("username").send_keys(u"yuzhu")
    browser.find_element_by_name("password").send_keys(u"yu56789")

    browser.find_element_by_xpath("//*[@id=\"fm1\"]/div[4]/button[1]").click()

    # 4a窗口的句柄
    handle_4a = browser.current_window_handle

    # 进入商合平台
    browser.find_element_by_xpath(
        "//*[@id=\"p_p_id_appcoll2_WAR_towerportlet_\"]/div/div/div/div/ul/li[11]/a[2]").click()

    # 处理新打开的窗口
    handles = browser.window_handles


    # 切换窗口
    for handle in handles:
        if handle != handle_4a:
            # print handle
            # 切换至新窗口，进入商合代办列表
            browser.switch_to.window(handle)
            # 进入商合平台代办列表
            browser.get(
                'http://www.eshop.chinatowercom.cn:8080/eshop/purchase/toPurchaseTask.do?shopCode=jtjcsd&tabFlag=onlinePurchase')

            # 判断购物车是否为空
            search_str = "//*[@id=\"mycart_count\"]"
            if str(browser.find_element_by_xpath(search_str).text) != "0":
                # 清空购物车
                # 点击  购物车
                time.sleep(2)
                search_str = "//*[@id=\"divCart\"]/div[1]/span[2]/a"
                browser.find_element_by_xpath(search_str).click()
                try:
                    time.sleep(2)
                    search_str = "//*/div[@name=\"shopCartDiv\"]/div[2]/table[3]/tbody/tr/td[2]/a/img"
                    browser.find_element_by_xpath(search_str).click()
                   # 处理弹出对话框
                    try:
                        time.sleep(3)
                        search_str = "//*[@id=\"artPlusConfirmyes\"]"
                        browser.find_element_by_xpath(search_str).click()
                    except:
                        pass
                except:
                    pass
                time.sleep(2)
                browser.get(
                    'http://www.eshop.chinatowercom.cn:8080/eshop/purchase/toPurchaseTask.do?shopCode=jtjcsd&tabFlag=onlinePurchase')

            # 开始进行逐条采购,
            flag_proceding = True
            while flag_proceding:
                # try:
                # 选择第一条记录，如果没有则出错，跳转至except进行错误处理
                browser.find_element_by_xpath("// *[ @ id = \"pool-content\"] / li[1] / a[1]").click()
                time.sleep(4)


                search_str = "//*[@id=\"forPage\"]/div/span"
                category =  str(browser.find_element_by_xpath(search_str).text)[3::]


                if category == "非单管塔":
                    unstandard_tower(browser,handles)
                elif category == "单管塔":
                    single_pipe_tower(browser,handles)
                elif category == "设计_铁塔类":
                    design(browser)
                elif category == "监理_铁塔类":
                    supervision(browser)
                else:
                    cabinet(browser)

                # 跳转页面
                browser.get(
                    'http://www.eshop.chinatowercom.cn:8080/eshop/purchase/toPurchaseTask.do?shopCode=jtjcsd&tabFlag=onlinePurchase')


            break

if __name__ == '__main__':
    while True:
        try:
            browser_chrome = webdriver.Chrome()
            main(browser_chrome)
        except:
            browser_chrome.quit()