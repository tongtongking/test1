# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import re
import pandas as pd


def get_page_info(keys,year,num):

    '''  '''

    cggg=[]
    bggg=[]
    jggg=[]
    teli=[]
    headers={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Host':'www.hngp.gov.cn',
    'Pragma':'no-cache',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',

    }
    

    for x in range(1,num+1):
        url='http://www.hngp.gov.cn/henan/search?&keyword={0}&year={1}&pageNo={2}'.format(keys.decode('gbk').encode('utf-8'),year,x)
        print x
        # url='http://www.hngp.gov.cn/henan/ggcx?appCode=H60&channelCode=0101&bz=0&pageSize=10&pageNo=%d'%n
        # url='http://www.hngp.gov.cn/henan/ggcx?appCode=H60&channelCode=0101&bz=0&pageSize=10&pageNo=1'%n
        r=requests.get(url,headers=headers)
        soup=BeautifulSoup(r.content,"lxml")
        lines=soup.findAll('div',class_="BorderBlue NoBorderTop Padding5")
        for i in lines:
            sb=i.findAll('li')
            for j in sb:
                with open('D:\\yinghao\\name_list.txt','a+')as t:
                    t.write(j.get_text().encode('utf-8'))
                try:
                    date=j.find('span').get_text().replace('-','/')
                    #ids= '/'+j.find('a')['href'][22:38]
                    ids= 'http://www.hngp.gov.cn/'+j.find('a')['href']
                    print ids


                    r1=requests.get(ids)
                    soup_1=BeautifulSoup(r1.content,'lxml')
                    z=soup_1.findAll('script')
                    sb_1=re.compile('/webfile/.*?\.htm')
                    for i in z:
                        if '.htm' in str(i):
                            zzz='http://www.hngp.gov.cn'+re.search(sb_1,str(i)).group()
                            #print zzz
                            if '/cggg/' in zzz:
                                try:
                                    with open('D:\\yinghao\\cggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')
                                        
                                        f1.write(j.get_text().encode('utf-8')+'\n')
                                        
                                        f1.write(ids+'\n')
                                    cggg.append(ids)
                                    cggg.append(j.get_text().encode('utf-8'))

                                    time.sleep(4)
                                    r2=requests.get(zzz)
                                    soup2=BeautifulSoup(r2.content,"lxml")
                                    ss=soup2.findAll('p')
                                    for i in ss:
                                        # print i
                                        with open('D:\\yinghao\\cggg-%s.txt'%year,'a')as f1:
                                            f1.write(i.get_text().encode('utf-8')+'\n')
                                finally:
                                    with open('D:\\yinghao\\cggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')



                            elif '/jggg/' in zzz:
                                try:
                                    with open('D:\\yinghao\\jggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')
                                        f1.write(j.get_text().encode('utf-8')+'\n')
                                        f1.write(ids+'\n')

                                    jggg.append(ids)
                                    jggg.append(j.get_text().encode('utf-8'))

                                    time.sleep(4)
                                    r2=requests.get(zzz)
                                    soup2=BeautifulSoup(r2.content,"lxml")
                                    ss=soup2.findAll('p')
                                    for i in ss:
                                        # print i
                                        with open('D:\\yinghao\\jggg-%s.txt'%year,'a')as f1:
                                            f1.write(i.get_text().encode('utf-8')+'\n')
                                finally:
                                    with open('D:\\yinghao\\jggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')



                            elif '/bggg/' in zzz:
                                try:
                                    with open('D:\\yinghao\\bggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')
                                        f1.write(j.get_text().encode('utf-8')+'\n')
                                        f1.write(ids+'\n')

                                    bggg.append(ids)
                                    bggg.append(j.get_text().encode('utf-8'))

                                    time.sleep(4)
                                    r2=requests.get(zzz)
                                    soup2=BeautifulSoup(r2.content,"lxml")
                                    ss=soup2.findAll('p')
                                    for i in ss:
                                        # print i
                                        with open('D:\\yinghao\\bggg-%s.txt'%year,'a')as f1:                                    
                                            f1.write(i.get_text().encode('utf-8')+'\n')
                                finally:
                                    with open('D:\\yinghao\\bggg-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')



                            else:
                                try:
                                    with open('D:\\yinghao\\teli-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')
                                        f1.write(j.get_text().encode('utf-8')+'\n')
                                        f1.write(ids+'\n')

                                    teli.append(ids)
                                    teli.append(j.get_text().encode('utf-8'))

                                    time.sleep(4)
                                    r2=requests.get(zzz)
                                    soup2=BeautifulSoup(r2.content,"lxml")
                                    ss=soup2.findAll('p')
                                    for i in ss:
                                        # print i
                                        with open('D:\\yinghao\\teli-%s.txt'%year,'a')as f1:                                    
                                            f1.write(i.get_text().encode('utf-8')+'\n')
                                finally:
                                    with open('D:\\yinghao\\teli-%s.txt'%year,'a')as f1:
                                        f1.write('\n'+'='*30+'\n')
                                
                except:
                    pass
        
if __name__=='__main__':
    keys=raw_input('keys')
    year=raw_input('year')
    num=int(input('page-index'))
    get_page_info(keys,year,num)
    
