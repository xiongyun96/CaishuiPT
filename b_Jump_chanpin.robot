#1.小艾卫士验证产品能否正常打开
#2.ABC财税专家验证产品能否正常打开
#3.财税专家小程序验证产品能否正常打开
#4.ABC4000电子申报验证产品能否正常打开
#5.艾易票验证产品能否正常打开
#6.艾易税智慧申报验证产品能否正常打开
#7.财税经验证书验证产品能否正常打开
#8.财税会员验证产品能否正常打开
#9.电子税局验证产品能否正常打开
#10.微众税银验证产品能否正常打开
#11.车购税委托代征管理系统验证产品能否正常打开
#12.所得税汇算清缴软件验证产品能否正常打开

*** Settings ***
Library      SeleniumLibrary
Library      Screenshot
Library      Collections
Library      B_产品.py

Suite Setup  Run keywords    login_ucchanpin  18008450000  1234567x
              ...   AND       del_UCguanggao1
              ...   AND       chanpin
Suite Teardown      out
*** Test Cases ***
1.小艾卫士验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    xiaoaiweishi
    ${yz1}=          xiaoaiweishi_yz
    log to console    ${yz1}
    should contain    ${yz1}    小艾卫士系统介绍
    SLEEP  3

2.ABC财税专家验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ABCcaishuizhuanjia
    ${yz2}=          ABCcaishuizhuanjia_yz
    log to console    ${yz2}
    should contain    ${yz2}    ABC财税专家软件是艾博克公司精心打造的
    SLEEP  3


3.财税专家小程序验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    caishuizhuanjia
    ${yz3}=          caishuizhuanjia_yz
    log to console    ${yz3}
    should contain    ${yz3}    随时记录生产经营过程中产生的收支流水，自动生成二栏式账簿，一键查看经营收支账和经营利润表。
    SLEEP  3

4.ABC4000电子申报验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    ABC400dianzishengbao
    ${yz3}=          ABC400dianzishengbao_yz
    log to console    ${yz3}
    should contain    ${yz3}    ABC4000电子申报缴税软件是属于“湖南省税务局电子申报缴税系统”的一种电子申报方式
    SLEEP  3

5.艾易票验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    aiyipiao
    ${yz4}=          aiyipiao_yz
    log to console    ${yz4}
    should contain    ${yz4}    艾易票为中小微企业提供一站式发票全流程闭环管理
    SLEEP  3

6.艾易税智慧申报验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    aysdianzishenbao
    ${yz5}=          aysdianzishenbao_yz
    log to console    ${yz5}
    should contain    ${yz5}    艾易税电子申报软件是ABC4000的升级版
    SLEEP  3

7.财税经验证书验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    caishuizhengshu
    ${yz6}=          caishuizhengshu_yz
    log to console    ${yz6}
    should contain    ${yz6}    ABC财税经验证书介绍
    SLEEP  3

8.财税会员验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    caishuihuiyuan
    ${yz7}=          caishuihuiyuan_yz
    log to console    ${yz7}
    should contain    ${yz7}    会员开通专属通道
    SLEEP  3

9.电子税局验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    dianzishuiju
    ${yz8}=          dianzishuiju_yz
    log to console    ${yz8}
    should contain    ${yz8}    目前电子税务局已经在湖南税务推行使用受到广大纳税人的一致好评
    SLEEP  3

10.微众税银验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    weizhongshuiyin
    ${yz9}=          weizhongshuiyin_yz
    log to console    ${yz9}
    should contain    ${yz9}    湖南税务联合多家银行开展“银税服务”活动
    SLEEP  3

11.车购税委托代征管理系统验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    chegoushui
    ${yz9}=          chegoushui_yz
    log to console    ${yz9}
    should contain    ${yz9}    车购税委托代征管理系统是为进一步提高征管效益、优化纳税服务，以核心征管系统为依托
    SLEEP  3

12.所得税汇算清缴软件验证产品能否正常打开
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    suodeshui
    ${yz9}=          suodeshui_yz
    log to console    ${yz9}
    should contain    ${yz9}    “汇算清缴”是在湖南省国家税务局的业务指导下，全新开发的
    SLEEP  3




