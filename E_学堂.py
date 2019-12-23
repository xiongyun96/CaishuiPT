from selenium import webdriver
import time
#双击
from selenium.webdriver.common.action_chains import ActionChains

from Global_variable import *
#--------------------------------------------------------------------------------------------------#

driver=webdriver.Chrome()
driver.implicitly_wait(10)


#财税平台--登录
def login_caishui():
    time.sleep(2)
    driver.get(caisuiURL)
    driver.maximize_window()
def login_ucxuetang(username,pwd):
    time.sleep(2)
    ZH=driver.find_element_by_css_selector('input[placeholder="用户名/手机号"]')
    ActionChains(driver).double_click(ZH).perform()  # 双击
    ZH.send_keys(username)

    MM=driver.find_element_by_css_selector('input[id="login_password"]')
    ActionChains(driver).double_click(MM).perform()  # 双击
    MM.send_keys(pwd)

    time.sleep(2)
    driver.find_element_by_css_selector('input[value="登录"]').click()

#×掉UC弹框广告---------------------------------------------------------------------------------------------------------------------------------
def del_UCguanggaoXuetang():
    time.sleep(3)
    #如果找不到元素报异常，直接跳过
    try:
        xsjifen1=driver.find_element_by_xpath('//div//span[@class="layui-layer-setwin"]//a')
        ActionChains(driver).double_click(xsjifen1).perform()    #双击
    except:
        pass

#学堂--退出
def uckt_login_exit():
    time.sleep(2)
    #鼠标悬浮在头像上
    yidong=driver.find_element_by_xpath('//*[@id="loginUser"]/div[3]/div')
    ActionChains(driver).move_to_element(yidong).perform()
    #点击退出并确定
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="logout"]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="layui-layer100001"]/div[3]/a[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginheaddiv"]/a[1]').click()

def get1111():
    cha=driver.find_element_by_xpath('//*[@id="layui-layer2"]/span[1]/a')
    get=cha.get.attribute('outerHTML')
    print(get)
    return get



#进入学堂
def xuetang():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div[1]/ul/li[6]/a').click()

#一、搜索课程
def sousuokecheng(kecheng):
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="schooltext"]').send_keys(kecheng)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="schoolsearch"]/i').click()
#验证搜索课程不存在时，返回值为0
def sousuokecheng_yz():
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
       # 检查搜索的标题
    time.sleep(3)
    yz2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/p').text
    time.sleep(2)
    driver.close()
        # 切回原窗口
    driver.switch_to.window(mainwindow)
    print(yz2)
    return  yz2


#验证学习免费课程
def mianfeikecheng():
        # 切换新窗口
    yuanchuangkou = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到搜索结果页面
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/a/div/div[2]').click()
    time.sleep(2)
    driver.close()
        #点击课程后跳转到课程详情页面
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到课程基本信息页面（开始学习）
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ksxx"]').click()
    time.sleep(2)
    driver.close()
        #点击开始学习后跳转到学习页面
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到课程学习页面
    time.sleep(2)
    neirong=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/span[1]').text
    time.sleep(2)
    driver.close()
        # 切回原窗口
    driver.switch_to.window(yuanchuangkou)
    print(neirong)
    return neirong


#验证会员学习付费课程
def fufeikecheng():
        # 切换新窗口
    yuanchuangkou = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到搜索结果页面
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/a/div/div[2]').click()
    time.sleep(2)
    driver.close()
        #点击课程后跳转到课程详情页面
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    time.sleep(3)
    anniu=driver.find_element_by_xpath('//*[@id="ksxx"]').text
    print(anniu)
    return  anniu

#验证非会员学习付费课程
def fufeikecheng1():
        # 切换新窗口
    yuanchuangkou = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到搜索结果页面
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/a/div/div[2]').click()
    time.sleep(2)
    driver.close()
        #点击课程后跳转到课程详情页面
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    time.sleep(3)
    anniu=driver.find_element_by_xpath('//*[@id="ljpay"]').text
    print(anniu)
    return  anniu

#进入搜索课程页面详情页
def fufeikecheng2():
        # 切换新窗口
    yuanchuangkou = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #到搜索结果页面
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/a/div/div[2]').click()
    time.sleep(2)
    driver.close()
        #点击课程后跳转到课程详情页面
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    time.sleep(2)


#课程详情老师介绍点击关注
def guanzhu():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]').click()
    time.sleep(3)
    #检查状态变成'已关注'
    zt=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]').text
    print(zt)
    return zt
# 课程详情老师介绍取消关注
def qxguanzhu():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="layui-layer-btn layui-layer-btn-"]/a').click()
    time.sleep(2)
    # 检查状态十分变成'关注'
    zt1 = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[1]').text
    print(zt1)
    return zt1

#获取课程老师的名字
def name():
    na=driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[2]/div[2]/div[1]/a/span/h4').text
    print(na)
    return na
#进入我的课堂获取第一个老师的名字
def myclass():
    time.sleep(2)
    # 鼠标悬浮在头像上
    yidong = driver.find_element_by_xpath('//*[@id="loginUser"]/div[3]/div')
    ActionChains(driver).move_to_element(yidong).perform()

    driver.find_element_by_xpath('//*[@id="loginUser"]/div[3]/div/div[2]/ul/a[5]/li/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="external-frame"]/div[3]/div[1]/span[3]').click()

    ls=driver.find_element_by_xpath('//*[@id="external-frame"]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/p').text
    print(ls)
    return ls




#收藏和取消课程
def shoucangkc():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="fenxiang"]/div/i').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="layui-layer-btn layui-layer-btn-"]/a').click()
    driver.find_element_by_xpath('//*[@id="scicon"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@class="layui-layer-btn layui-layer-btn-"]/a[1]').click()

    kechengming=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]').text
    print(kechengming)
    return kechengming

#进入我的课堂获取第一个收藏的课程
def shoucangyz():
    time.sleep(2)
    # 鼠标悬浮在头像上
    yidong = driver.find_element_by_xpath('//*[@id="loginUser"]/div[3]/div')
    ActionChains(driver).move_to_element(yidong).perform()

    driver.find_element_by_xpath('//*[@id="loginUser"]/div[3]/div/div[2]/ul/a[5]/li/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="external-frame"]/div[3]/div[1]/span[2]').click()

    kc=driver.find_element_by_xpath('//*[@id="external-frame"]/div[4]/div[1]/div[2]/ul/li[1]/h5').text
    print(kc)
    return kc



#关闭浏览器
def out():
    driver.quit()

