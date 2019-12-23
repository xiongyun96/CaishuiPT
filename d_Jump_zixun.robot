#1.小艾财税周刊 验证能否跳转到相应页面
#2.热门资讯 验证能否跳转到相应页面
#3.热词推荐验证能否跳转到相应页面
#4.帮友热议验证能否跳转到相应页面



*** Settings ***
Library      SeleniumLibrary
Library      Screenshot
Library      Collections
Library      D_资讯.py

Suite Setup  Run keywords    login_uczixun  18008450000  1234567x
              ...   AND       del_UCguanggao3
              ...   AND       zixun
Suite Teardown      out
*** Test Cases ***
1.小艾财税周刊 验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ${yz2}=     xiaoaizhoukan
    ${yz1}=     xiaoaizhoukan_yz
    log to console    ${yz1}
    should contain    ${yz1}    ${yz2}
    SLEEP  3

2.热门资讯 验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ${yz2}=     remenzixun_yz1
    remenzixun
    ${YZ3}=     remenzixun_yz2
    log to console    ${yz2}
    log to console    ${yz3}
    should contain    ${yz3}    ${yz2}
    SLEEP  3

3.热词推荐验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ${yz4}=     recituijian_yz1
    recituijian
    ${YZ5}=     recituijian_yz2
    log to console    ${yz4}
    log to console    ${yz5}
    should contain    ${yz5}    ${yz4}
    SLEEP  3

4.帮友热议验证能否跳转到相应页面
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ${yz6}=     bangyoureyi_yz1
    bangyoureyi
    ${YZ7}=     bangyoureyi_yz2
    log to console    ${yz6}
    log to console    ${yz7}
    should contain    ${yz7}    ${yz6}
    SLEEP  3

