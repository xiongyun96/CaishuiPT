from selenium import webdriver
import time
#双击
from selenium.webdriver.common.action_chains import ActionChains

from Global_variable import *
#--------------------------------------------------------------------------------------------------#

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.find_element_by_xpath()
#财税平台--登录
def login_ucchanpin(username,pwd):
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
def del_UCguanggao1():
    time.sleep(3)
    #如果找不到元素报异常，直接跳过
    try:
        xsjifen1=driver.find_element_by_xpath('//div//span[@class="layui-layer-setwin"]//a')
        ActionChains(driver).double_click(xsjifen1).perform()    #双击
    except:
        pass


#进入产品页面
def chanpin():
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="header"]/div/div/div[3]/div[1]/ul/li[2]/a').click()


#一、进入'小艾卫士'
def xiaoaiweishi():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[1]/li/img').click()
    #验证进入'小艾卫士'页面是否正确
def xiaoaiweishi_yz():
    time.sleep(2)
    # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查''小艾卫士系统介绍''
    time.sleep(3)
    xaws=driver.find_element_by_xpath('/html/body/div[3]/div[1]/p[1]').text
    driver.close()
        #切回原窗口
    driver.switch_to.window(mainwindow)
    print(xaws)
    return xaws


#二、进入'ABC财税专家'
def ABCcaishuizhuanjia():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[2]/li/div').click()
    #验证进入'财税专家'页面是否正确
def ABCcaishuizhuanjia_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘ABC财税专家软件是艾博克公司精心打造的’
    time.sleep(2)
    cszj = driver.find_element_by_xpath('/html/body/div[3]/div[1]/p[2]').text
    driver.close()
        # 切回原窗口
    driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#三、进入'财税专家小程序'
def caishuizhuanjia():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[3]/li/div').click()
    #验证进入'财税专家小程序'页面是否正确
def caishuizhuanjia_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘随时记录生产经营过程中产生的收支流水，自动生成二栏式账簿，一键查看经营收支账和经营利润表。’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div/div/span').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#四、进入ABC4000电子申报
def ABC400dianzishengbao():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[4]/li/img').click()
    #验证进入ABC4000电子申报页面是否正确
def ABC400dianzishengbao_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘ABC4000电子申报缴税软件是属于“湖南省税务局电子申报缴税系统”的一种电子申报方式’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[1]/p[2]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#五、进入'艾易票'
def aiyipiao():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[5]/li/img').click()
    #验证进入'艾易票'页面是否正确
def aiyipiao_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘艾易票为中小微企业提供一站式发票全流程闭环管理’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/span').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#六、进入'艾易税电子申报'
def aysdianzishenbao():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[6]/li/img').click()
        #验证进入'艾易税电子申报'页面是否正确
def aysdianzishenbao_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘艾易税电子申报软件是ABC4000的升级版’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/span').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj

#七、进入'财税经验证书'
def caishuizhengshu():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[7]/li/img').click()
        #验证进入'财税经验证书'页面是否正确
def caishuizhengshu_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘ABC财税经验证书介绍’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[1]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj

#八、进入'财税会员'
def caishuihuiyuan():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[8]/li/img').click()
    #验证进入'财税会员'页面是否正确
def caishuihuiyuan_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘会员开通专属通道’
    try:
        time.sleep(2)
    #     # 拖动滚轮到可见的元素去
    # target = driver.find_element_by_xpath("/html/body/div[4]/div[3]/a")
    # driver.execute_script("arguments[0].scrollIntoView();", target)
    # time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/p[1]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#九、进入'电子税局'
def dianzishuiju():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[9]/li/img').click()
    #验证进入'电子税局'页面是否正确
def dianzishuiju_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘目前电子税务局已经在湖南税务推行使用受到广大纳税人的一致好评’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[5]/p[2]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#十、进入'微众税银'
def weizhongshuiyin():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[10]/li/img').click()
    #验证进入'微众税银'页面是否正确
def weizhongshuiyin_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘企业凭借良好纳税信用可通过“湖南微众税银公众服务平台” www.vzoom.com免费申请信用贷款’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[1]/p[2]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj

#十一、进入'车购税委托代征管理系统'
def chegoushui():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[11]/li/img').click()
    #验证进入'车购税委托代征管理系统'页面是否正确
def chegoushui_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘车购税委托代征管理系统是为进一步提高征管效益、优化纳税服务，以核心征管系统为依托’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[1]/p[2]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj

#十二、进入'所得税汇算清缴软件'
def suodeshui():
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[3]/ul/a[12]/li/img').click()
    #验证进入'所得税汇算清缴软件'页面是否正确
def suodeshui_yz():
    time.sleep(2)
        # 切换新窗口
    mainwindow = driver.current_window_handle
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        #检查‘“汇算清缴”是在湖南省国家税务局的业务指导下，全新开发的基于云平台的汇算清缴电子申报缴税系统。’
    try:
        time.sleep(2)
        cszj = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/p[2]').text
    finally:
        driver.close()
        # 切回原窗口
        driver.switch_to.window(mainwindow)
    print(cszj)
    return cszj


#关闭浏览器
def out():
    driver.quit()

