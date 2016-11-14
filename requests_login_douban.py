# -*-coding=utf-8 -*-
'''
本程序模拟登陆豆瓣网站,并修改签名.签名尽量采用英文或数字,如果需要使用中文请注意编码!
'''

import requests
from bs4 import BeautifulSoup
import time

def get_picture(url,titlename):
    s=requests.Session()
    cont=s.get(url)
    time.sleep(2)
    try:
        src=parser(cont.content,'img','src',id="captcha_image")
        di=parser(cont.content,'input','value',type="hidden",name="captcha-id")
        print id
        print src
        st=raw_input('请输入验证码:')
    except:
        print 'Get nothing!'
        st=di=''
    data={'form_email':'xxxxxxxxxx',#你注册的手机号码
        'form_password':'xxxxxxxxx',#你的密码
        'source':'index_nav',
        'redir':'https://www.douban.com/',
        'captcha-id':di,
        'captcha-solution':st,
        'login':'登录'
    }
    r=s.post(url,data=data)
    b=s.get('https://www.douban.com/mine/')
    time.sleep(2)
    ck=parser(b.content,'input','value',type='hidden',name='ck')
    print ck
    s.post('https://www.douban.com/j/people/139671401/edit_signature',data={"signature":titlename,'ck':ck})#该链接因用户不同而略有不同
    b=s.get('https://www.douban.com/mine/')
    time.sleep(2)
    if titlename in b.content:
        print '登陆成功!'
    else:
        print 'Login Failed!'

def parser(source,tag,attr,**kwg):
    soup=BeautifulSoup(source,'lxml',from_encoding='utf-8')
    result=soup.find(name=tag,attrs=kwg)
    return result[attr]
if __name__ == '__main__':
    url='https://accounts.douban.com/login'
    titlename=raw_input('请输入签名:')
    get_picture(url,titlename)
