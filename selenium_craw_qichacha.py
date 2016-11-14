# -*- coding=utf-8 -*-
# user/env/bin python

'''
本程序操作chrome浏览器抓取企查查网站的全国公司注册信息！
在运行程序之前请首先下载driverchrome插件,并将其放在chrome.exe同一个文件夹中,
同时将插件配置到环境变量中,即可运行程序,程序中有不妥的地方欢迎fork me!
author：TongtongKing
验证码部分需要手动辅助验证,通过之后即可自动抓取信息!

'''

import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


with open('num9.sql')as ff:
    company_name=ff.readlines()
b=webdriver.Chrome()#.PhantomJS(executable_path=r'C:\Python27\phantomjs-2.1.1-windows\bin\phantomjs.exe')
b.get('http://www.qichacha.com/user_login')


#输入并提交注册名
b.find_element_by_name("nameNormal").send_keys('注册的手机号码')
print '1---'
#输入并提交密码
b.find_element_by_name("pwdNormal").send_keys('密码')
print '2---'

i=1
time.sleep(2)
try:
    #尝试解锁25次
    while i<=25:
        i+=1
        element=b.find_element_by_id('nc_1_n1z')#被拖动元素的起始位置
        target=b.find_element_by_class_name("nc_voice")#被拖动元素的终点位置
        ActionChains(b).drag_and_drop(element, target).perform()#拖动元素
        ActionChains(b).drag_and_drop(target,element).perform()
        print i
finally:
    print '解锁成功！'
time.sleep(4)
#点击提交按钮
b.find_element_by_tag_name("button").click()

print 'goto heighter'

c=1
for name in company_name:
    print '第'+str(c)+'家公司！',name.replace('\n','').decode('utf-8').encode('utf-8')
    with open('sql_craw_info.sql','a')as h:
        h.write(name.decode('utf-8').encode('utf-8'))
    time.sleep(3)#等待页面跳转
    
    #页面跳转成功即表示登录成功
    try:
        b.get('http://www.qichacha.com/search?key=%s&index=0'%name)
        time.sleep(3)

        soup=BeautifulSoup(b.page_source,'lxml',from_encoding='utf-8')
        ss=soup.findAll("a")
        j=1
        for s in ss:
            if 'class="text-priamry"' in str(s):
                url='http://www.qichacha.com'+s['href']
                b.get(url)
                time.sleep(3)
                with open('%d.txt'%j,'a')as nf:
                    nf.write('\n'+'-'*30+'\n')
                    nf.write(b.page_source.encode('utf-8'))
                    nf.write('\n'+'-'*30+'\n')
                j+=1
    except:
        print '公司信息不存在或者系统需要再次验证!!!!!'
        with open('sql_craw_info.sql','a')as h:
            h.write('\n'+'公司信息不存在或者系统需要再次验证!!!!!'.encode('utf-8'))
        continue
    c+=1

b.close()


