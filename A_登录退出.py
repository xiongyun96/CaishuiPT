from selenium import webdriver
import time
#显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#双击
from selenium.webdriver.common.action_chains import ActionChains
from Global_variable import *
#--------------------------------------------------------------------------------------------------#

driver=webdriver.Chrome()
driver.implicitly_wait(10)

#财税平台--登录
def login_uc(username,pwd):
    time.sleep(2)
    driver.get(caisuiURL)
    driver.maximize_window()

    time.sleep(3)
    ZH=driver.find_element_by_css_selector('input[placeholder="用户名/手机号"]')
    ActionChains(driver).double_click(ZH).perform()  # 双击
    ZH.send_keys(username)

    MM=driver.find_element_by_css_selector('input[id="login_password"]')
    ActionChains(driver).double_click(MM).perform()  # 双击
    MM.send_keys(pwd)

    time.sleep(3)
    driver.find_element_by_css_selector('input[value="登录"]').click()

#robot登录信息错误，验证页面是否存在‘短信验证码登陆’字段
def longin_uc_yz1():
    time.sleep(3)
    yanz1=driver.find_element_by_css_selector('div[class="login_duanxin"]').text
    print(yanz1)
    return yanz1
#robot登录信息正确，验证页面是否存在‘个人中心’字段
def longin_uc_yz2():
    time.sleep(3)
    yanz2=driver.find_element_by_xpath('//*[@id="dh_left"]/li[1]').text
    print(yanz2)
    return yanz2

#uc中心--退出
def uczx_login_exit():
    time.sleep(2)
    #鼠标悬浮在头像上
    yidong=driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div[3]')
    ActionChains(driver).move_to_element(yidong).perform()
    #点击退出并确定
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="logout"]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@class="layui-layer-btn layui-layer-btn-"]/a[1]').click()

def uczx_login_exit_yz():
    time.sleep(3)
    # robot退出后验证页面是否存在‘通知公告’字段
    denglu=driver.find_element_by_xpath('//*[@id="carousel-example-generic"]/div/div[2]/div/p').text
    print(denglu)
    return denglu

#×掉UC弹框广告---------------------------------------------------------------------------------------------------------------------------------
def del_UCguanggao():
    time.sleep(3)
    #如果找不到元素报异常，直接跳过
    try:
        xsjifen1=driver.find_element_by_xpath('//div//span[@class="layui-layer-setwin"]//a')
        ActionChains(driver).double_click(xsjifen1).perform()    #双击
    except:
        pass

#关闭浏览器
def out():
    driver.quit()



#运营管理系统--登录
def login_yyglxt(name,pwd):
    time.sleep(2)
    driver.get(yunyingURL)
    driver.maximize_window()
    time.sleep(3)
    #输入账号密码登录
    time.sleep(3)
    ZH = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[1]/input')
    ActionChains(driver).double_click(ZH).perform()     # 双击
    ZH.send_keys(name)
    ZH = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/input')
    ActionChains(driver).double_click(ZH).perform()      # 双击
    ZH.send_keys(pwd)

    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[4]/input').click()

#robot登录信息错误，验证页面是否存在‘忘记密码’字段
def login_yyglxt_yz1():
    time.sleep(2)
    YZ1=driver.find_element_by_xpath('//*[@id="forgot_password"]').text
    print(YZ1)
    return YZ1
#robot登录信息正确，验证页面是否存在‘我的销售管理’字段
def login_yyglxt_yz2():
    time.sleep(2)
    YZ2=driver.find_element_by_xpath('//*[@id="main_ileft"]/div[1]/ul/li[1]/div/a/ss').text
    print(YZ2)
    return YZ2

#运营管理系统--退出并确定
def yyglxt_login_exit():
    time.sleep(3)
    #退出登录并确定
    driver.find_element_by_xpath('//*[@id="main_itop_l_ny"]/div[3]/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()

# robot退出后验证页面是否存在‘忘记密码’字段
def yyglxt_login_exit_yz1():
    time.sleep(2)
    exit=driver.find_element_by_xpath('//*[@id="forgot_password"]').text
    print(exit)
    return exit


#浏览器后退
def houtui():
    driver.back()