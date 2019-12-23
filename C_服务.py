from selenium import webdriver
import time
#双击
from selenium.webdriver.common.action_chains import ActionChains

from Global_variable import *
#--------------------------------------------------------------------------------------------------#

driver=webdriver.Chrome()
driver.implicitly_wait(10)


#财税平台--登录
def login_ucfuwu(username,pwd):
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

#×掉UC弹框广告---------------------------------------------------------------------------------------------------------------------------------
def del_UCguanggao2():
    time.sleep(3)
    #如果找不到元素报异常，直接跳过
    try:
        xsjifen1=driver.find_element_by_xpath('//div//span[@class="layui-layer-setwin"]//a')
        ActionChains(driver).double_click(xsjifen1).perform()    #双击
    except:
        pass



#进入服务页面
def fuwu():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div[1]/ul/li[3]/a').click()

#一、进入'帮助中心'
def bangzhuzhongxin():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[1]/a/p[1]/i').click()
    #验证进入'帮助中心'页面是否正确
def bangzhuzhongxin_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查''知识与帮助中心''
    try:
        time.sleep(3)
        xaws=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/a').text
    finally:
        driver.close()
        #切回原窗口
        driver.switch_to.window(mainwindow)
    print(xaws)
    return xaws


#二、进入'申报服务续费'
def shenbaofuwuxufei():
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]/a/p[1]/i').click()
    # ActionChains(driver).double_click(cc).perform()  # 双击
    #验证进入'申报服务续费'页面是否正确
def shenbaofuwuxufei_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查''财税服务产品续费''
    try:
        time.sleep(3)
        xaws=driver.find_element_by_xpath('/html/body/div[2]/div[1]').text
    finally:
        driver.close()
        #切回原窗口
        driver.switch_to.window(mainwindow)
    print(xaws)
    return xaws


#三、进入'忘记申报密码'
def wangjimima():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[3]/a/p[1]/i').click()
    #验证进入'忘记申报密码'页面是否正确
def wangjimima_yz():
    time.sleep(2)
    try:
        #检查''ABC电子申报企业信息 ''
        xaws=driver.find_element_by_xpath('//*[@id="external-frame"]/div[2]/ul/li[1]').text
    finally:
        # 后退
        driver.back()
    print(xaws)
    return xaws

#四、进入'更换绑定手机'
def genghuanshouji():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[4]/a/p[1]/i').click()
    #验证进入'更换绑定手机'页面是否正确
def genghuanshouji_yz():
    time.sleep(2)
    try:
        #检查''当前手机号 ''
        xaws=driver.find_element_by_xpath('//*[@id="updPhoneFrom"]/div[2]/label').text
    finally:
        driver.back()   #后退
    print(xaws)
    return xaws


#五、进入'实名认证'
def shimingrenzheng():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[5]/a/p[1]/i').click()
    #验证进入'实名认证'页面是否正确
def shimingrenzheng_yz():
    time.sleep(2)
    try:
        #检查''立即实名 ''
        xaws=driver.find_element_by_xpath('//*[@id="smrzClickDiv"]/span[2]').text
    finally:
        driver.back()   #后退
    print(xaws)
    return xaws

#六、进入'索取发票'
def suoqufapiao():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[7]/a/p[1]/i').click()
    #验证进入'索取发票'页面是否正确
def suoqufapiao_yz():
    time.sleep(2)
    try:
        #检查''索取发票 ''
        xaws=driver.find_element_by_xpath('//*[@id="external-frame"]/div[2]/ul/li[1]').text
    finally:
        driver.back()   #后退
    print(xaws)
    return xaws


#七、进入'账户充值'
def zhanghuchongzhi():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[8]/a/p[1]/i').click()
    #验证进入'账户充值'页面是否正确
def zhanghuchongzhi_yz():
    time.sleep(2)
    try:
        #检查''*备注：充值后不能退换! ''
        xaws=driver.find_element_by_xpath('//*[@id="external-frame"]/div/div[3]/p[4]').text
    finally:
        driver.back()   #后退
    print(xaws)
    return xaws


#八、进入'我的积分'
def wodejifen():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[9]/a/p[1]/i').click()
    #验证进入'我的积分'页面是否正确
def wodejifen_yz():
    time.sleep(2)
    try:
        #检查'' 【查看积分规则】''
        xaws=driver.find_element_by_xpath('//*[@id="rule"]').text
    finally:
        driver.back()   #后退
    print(xaws)
    return xaws


#九、进入'证书查询'
def zhengshuchaxun():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[10]/a/p[1]/i').click()
    #验证进入'证书查询'页面是否正确
def zhengshuchaxun_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    try:
        #检查'' ABC财税经验证书查询''
        time.sleep(3)
        xaws=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div').text
    finally:
        driver.close()
        #切回原窗口
        driver.switch_to.window(mainwindow)
    print(xaws)
    return xaws

#关闭浏览器
def out():
    driver.quit()

