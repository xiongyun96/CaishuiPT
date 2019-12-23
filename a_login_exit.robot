#1.uc登录成功后退出账号并能停留在首页
#2.yyglxt登录成功后退出账号并能停留在首页
#3.uc登录-输入错误的账号和正确的密码
#4.uc登录-输入正确的账号和错误的密码
#5.uc登录-输入错误的账号和错误的密码
#6.uc登录-输入正确的账号和正确的密码
#7.yyglxt登录-输入错误账号和正确密码
#8.yyglxt登录-输入正确账号和错误密码
#9.yyglxt登录-输入错误账号和错误密码
#10.yyglxt登录-输入正确的账号和正确的密码

*** Settings ***
Library      SeleniumLibrary
Library      Screenshot
Library      Collections
Library      A_登录退出.py

Suite Teardown   out
*** Test Cases ***
1.uc登录成功后退出账号并能停留在首页
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_uc           18008457724     1234567x
    del_UCguanggao
    uczx_login_exit
    ${yz5}=            uczx_login_exit_yz
    log to console      ${yz5}
    should contain      ${yz5}          通知公告
    sleep  2

2.yyglxt登录成功后退出账号并能停留在首页
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_yyglxt            880889          1234567x
    yyglxt_login_exit
    ${yz5}=            yyglxt_login_exit_yz1
    log to console      ${yz5}
    should contain      ${yz5}          忘记密码

3.uc登录-输入错误的账号和正确的密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_uc           0000111122225555     1234567x
    ${yz2}=           longin_uc_yz1
    log to console     ${yz2}
    should contain     ${yz2}         短信验证码登陆
    SLEEP  2

4.uc登录-输入正确的账号和错误的密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_uc           18008457722     123456789123456
    ${yz3}=           longin_uc_yz1
    log to console     ${yz3}
    should contain     ${yz3}         短信验证码登陆
    SLEEP  2

5.uc登录-输入错误的账号和错误的密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_uc           778899554412     4569855sadsad
    ${yz4}=           longin_uc_yz1
    log to console     ${yz4}
    should contain     ${yz4}         短信验证码登陆
    SLEEP  2

6.uc登录-输入正确的账号和正确的密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_uc           18008457721     1234567x
    ${yz1}=           longin_uc_yz2
    log to console     ${yz1}
    should contain     ${yz1}         个人中心
    SLEEP  2
    houtui
    SLEEP  2

7.yyglxt登录-输入错误账号和正确密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_yyglxt       45698745456498     1234567x
    ${yz2}=           login_yyglxt_yz1
    log to console     ${yz2}
    should contain     ${yz2}         忘记密码
    SLEEP  2

8.yyglxt登录-输入正确账号和错误密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_yyglxt       880889     54565498sadasdasd
    ${yz3}=           login_yyglxt_yz1
    log to console     ${yz3}
    should contain     ${yz3}         忘记密码
    SLEEP  2

9.yyglxt登录-输入错误账号和错误密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_yyglxt       656654512asdsad     54565498sadasdasd
    ${yz4}=           login_yyglxt_yz1
    log to console     ${yz4}
    should contain     ${yz4}         忘记密码
    SLEEP  2

10.yyglxt登录-输入正确的账号和正确的密码
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_yyglxt       880889     1234567x
    ${yz1}=           login_yyglxt_yz2
    log to console     ${yz1}
    should contain     ${yz1}         我的销售管理
    houtui
    SLEEP  2
