from selenium import webdriver
import time
#双击
from selenium.webdriver.common.action_chains import ActionChains

from Global_variable import *
#--------------------------------------------------------------------------------------------------#

driver=webdriver.Chrome()
driver.implicitly_wait(10)


#bat脚本测试
def bat():
    time.sleep(2)
    driver.get('http://www.manongjc.com/article/66636.html')
    te=driver.find_element_by_xpath('//*[text()="实现RobotFramework测试脚本失败自动重跑"]').text
    print(te)
    return te

#财税平台--登录
def login_uczixun(username,pwd):
    time.sleep(2)
    driver.get(caisuiURL)
    driver.maximize_window()

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
def del_UCguanggao3():
    time.sleep(3)
    #如果找不到元素报异常，直接跳过
    try:
        xsjifen1=driver.find_element_by_xpath('//div//span[@class="layui-layer-setwin"]//a')
        ActionChains(driver).double_click(xsjifen1).perform()    #双击
    except:
        pass



#进入资讯页面
def zixun():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div[1]/ul/li[4]/a').click()


#一、进入'小艾财税周刊'
def xiaoaizhoukan():
    time.sleep(2)
    biaoti=driver.find_element_by_xpath('//li[@title="小艾财税周刊"]//div[@class="zx_right_title"]/p').text
    driver.find_element_by_xpath('//li[@title="小艾财税周刊"]//div[@class="zx_right_title"]/p').click()
    print(biaoti)
    return biaoti
    #验证进入'小艾财税周刊'页面是否正确
def xiaoaizhoukan_yz():
    time.sleep(3)
      #检查''标题是否与外面的一样''
    xawd=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div[2]').text
    driver.back()    #后退
    print(xawd)
    return  xawd


#二、进入'热门资讯'
def remenzixun():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="hotContent"]/li[1]/a/img').click()
    #获取热门资讯第一个的标题
def remenzixun_yz1():
    time.sleep(3)
    zixun=driver.find_element_by_xpath('//*[@id="hotContent"]/li[1]/a/div[2]/p').text
    print(zixun)
    return zixun
    #进入第一个资讯，验证标题
def remenzixun_yz2():
    time.sleep(3)
      #检查''标题 ''
    xawd=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/h3').text
    driver.back()   #后退
    print(xawd)
    return  xawd


#三、进入'热词推荐'
def recituijian():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="hotLabel"]/div[2]/a[1]').click()
    #获取热词推荐第一个的热词
def recituijian_yz1():
    time.sleep(3)
    reci=driver.find_element_by_xpath('//*[@id="hotLabel"]/div[2]/a[1]').text
    print(reci)
    return reci
    #进入第一个热词，验证标题
def recituijian_yz2():
    time.sleep(3)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        # 检查热词的标题
    time.sleep(3)
    reci1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li').text
    driver.close()
        # 切回原窗口
    driver.switch_to.window(mainwindow)
    print(reci1)
    return reci1

#四、进入'帮友热议'
def bangyoureyi():
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="hotDiscussion"]/div/ul/li[1]/a/span').click()
    #获取帮友热议第一个的热词
def bangyoureyi_yz1():
    time.sleep(2)
    reci=driver.find_element_by_xpath('//*[@id="hotDiscussion"]/div/ul/li[1]/a/span').text
    print(reci)
    return reci
#进入第一个帮友热议，验证标题
def bangyoureyi_yz2():
    time.sleep(5)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        # 检查热词的标题
    time.sleep(5)
    reci1 = driver.find_element_by_xpath('//*[@id="xiangqing"]/ul[1]/li/h4').text
    driver.close()
        # 切回原窗口
    driver.switch_to.window(mainwindow)
    print(reci1)
    return reci1

#关闭浏览器
def out():
    driver.quit()

