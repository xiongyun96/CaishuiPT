*** Settings ***
Library      SeleniumLibrary
Library      Screenshot
Library      Collections
Library      E_学堂.py

Suite Setup    login_caishui
#              ...   AND       del_UCguanggaoXuetang
#              ...   AND       xuetang
#Suite Teardown   out
*** Test Cases ***
1.查询不存在的课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008459999  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     不存在课程查询不到
    ${SS1}=           sousuokecheng_yz
    log to console    ${SS1}
    should contain    ${SS1}    搜索与不存在课程查询不到有关的共0条记录
    uckt_login_exit

2.查询存在的课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008459999  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索免费课程专用
    ${SS2}=           sousuokecheng_yz
    log to console    ${SS2}
    should contain    ${SS2}    搜索与自动化搜索免费课程专用有关的共1条记录
    uckt_login_exit

3.验证非会员用户学习免费课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008457727  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng    自动化搜索免费课程专用
    ${SS3}=           mianfeikecheng
    log to console    ${SS3}
    should contain    ${SS3}    自动化搜索免费课程专用
    uckt_login_exit

4.验证会员用户学习免费课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008451111  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng    自动化搜索免费课程专用
    ${SS4}=           mianfeikecheng
    log to console    ${SS4}
    should contain    ${SS4}    自动化搜索免费课程专用
    uckt_login_exit

5.验证会员用户学习付费课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008451111  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    ${SS5}=           fufeikecheng
    log to console    ${SS5}

    should contain    ${SS5}       开始学习
    uckt_login_exit

6.验证非会员用户学习付费课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008457727  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    ${SS5}=           fufeikecheng1
    log to console    ${SS5}
    should contain    ${SS5}       立即购买
    uckt_login_exit

7.关注老师后当前的页面状态变化，并且我的课程关注讲师中存在该老师
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008452222  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    fufeikecheng2
    ${gz}=              guanzhu
    log to console      ${gz}
    ${name}=            name
    log to console      ${name}
    ${name1}=           myclass
    log to console      ${name1}
    should contain      ${gz}         已关注
    should contain      ${name}    ${name1}
    xuetang
    uckt_login_exit

8.取消关注老师当前的页面状态变化，并且我的课程关注讲师中不存在该老师
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008452222  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    fufeikecheng2
    ${gz}=              qxguanzhu
    log to console      ${gz}
    ${name}=            name
    log to console      ${name}
    ${name1}=           myclass
    log to console      ${name1}
    should contain      ${gz}      +关注
    should not contain      ${name1}   ${name}
    xuetang
    uckt_login_exit

9.收藏课程后，我的课程关注中显示相应课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008452222  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    fufeikecheng2
    ${kc}=              shoucangkc
    log to console      ${kc}
    ${sc}=            shoucangyz
    log to console      ${sc}
    should contain      ${sc}   ${kc}
    xuetang
    uckt_login_exit

10.取消收藏课程后，我的课程关注中显示相应课程
    [Teardown]        Run Keyword If Test Failed          Take Screenshot
    login_ucxuetang    18008452222  1234567x
    del_UCguanggaoXuetang
    xuetang
    sousuokecheng     自动化搜索付费课程专用
    fufeikecheng2
    ${kc}=              shoucangkc
    log to console      ${kc}
    ${sc}=            shoucangyz
    log to console          ${sc}
    should not contain      ${sc}   ${kc}
    xuetang
    uckt_login_exit
    out

