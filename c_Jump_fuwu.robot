#1.帮助中心验证能否跳转到相应页面
#2.申报服务续费验证能否跳转到相应页面
#3.忘记申报密码续费验证能否跳转到相应页面
#4.更换绑定手机验证能否跳转到相应页面
#5.实名认证验证能否跳转到相应页面
#6.索取发票验证能否跳转到相应页面
#7.账户充值验证能否跳转到相应页面
#8.我的积分验证能否跳转到相应页面
#9.证书查询验证能否跳转到相应页面

*** Settings ***
Library      SeleniumLibrary
Library      Screenshot
Library      Collections
Library      C_服务.py

Suite Setup  Run keywords    login_ucfuwu  18008450000  1234567x
              ...   AND       del_UCguanggao2
              ...   AND       fuwu
Suite Teardown    out
*** Test Cases ***
1.帮助中心验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    bangzhuzhongxin
    ${yz1}=     bangzhuzhongxin_yz
    log to console    知识与帮助中心
    log to console    ${yz1}
    should contain    ${yz1}    知识与帮助中心
    SLEEP  3

#2.申报服务续费验证能否跳转到相应页面
#    shenbaofuwuxufei
#    ${yz2}=     shenbaofuwuxufei_yz
#    log to console    财税服务产品续费
#    log to console    ${yz2}
#    should contain    ${yz2}    财税服务产品续费
#    SLEEP  3

3.忘记申报密码续费验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    wangjimima
    ${yz3}=     wangjimima_yz
    log to console    ABC电子申报企业信息
    log to console    ${yz3}
    should contain    ${yz3}    ABC电子申报企业信息
    SLEEP  3

4.更换绑定手机验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    genghuanshouji
    ${yz4}=     genghuanshouji_yz
    log to console    当前手机号
    log to console    ${yz4}
    should contain    ${yz4}    当前手机号
    SLEEP  3

5.实名认证验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    shimingrenzheng
    ${yz5}=     shimingrenzheng_yz
    log to console    立即实名
    log to console    ${yz5}
    should contain    ${yz5}    立即实名
    SLEEP  3

6.索取发票验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    suoqufapiao
    ${yz6}=     suoqufapiao_yz
    log to console    索取发票
    log to console    ${yz6}
    should contain    ${yz6}    索取发票
    SLEEP  3

7.账户充值验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    zhanghuchongzhi
    ${yz7}=     zhanghuchongzhi_yz
    log to console    *备注：充值后不能退换!
    log to console    ${yz7}
    should contain    ${yz7}    *备注：充值后不能退换!
    SLEEP  3

8.我的积分验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    wodejifen
    ${yz8}=     wodejifen_yz
    log to console    ${yz8}
    log to console    ${yz8}
    should contain    ${yz8}    查看积分规则 》
    SLEEP  3

9.证书查询验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    zhengshuchaxun
    ${yz9}=     zhengshuchaxun_yz
    log to console    ABC财税经验证书查询
    log to console    ${yz9}
    should contain    ${yz9}    ABC财税经验证书查询
    SLEEP  3
    out

