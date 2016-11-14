# -*- coding=utf-8 -*-

'''

http://www.hngp.gov.cn/
使用方法为：输入文本名称即可运行、输出

'''



import re
import pandas as pd


def write_into_excel(filename):
    
    '''本程序把从河南省政府采购网——采购信息栏抓取的文本内容，分类、写入excel表格'''
    
    with open(r'D:\yinghao\%s.txt'%filename)as f:
        st1=f.read()
        
    su=re.compile(' +')
    st2=su.sub('',st1)#正则表达式，替换文本中的空格
    
    namelist=re.compile("==============================\n(.*?)\n")
    sy=re.findall(namelist,st1)
    aa=st2.split('==============================')#分隔文件内容并存入列表
    aa.pop(0)
    lb=[]
    for i ,v in zip(aa,sy):
        # print i.decode('utf-8').encode('utf-8')
        l=[]
        
        #print i
        l.append(v.decode('utf-8'))
        #print len(v)
        s0=re.compile('采购单位：.*?\n|采购单位名称：.*?\n|招标人：.*?\n|招 标 人：.*?\n|招标单位.*?：.*?\n|采购人+?：.*?\n|采.+购.+人：.*?\n|项目单位：.*?\n')
        s00=re.compile('联系人：.*?联系电话.*?\n|联.*?系.*?人：.+女士|联.*?系.*?人：.+|项目负责人：.*?\n')
        s1=re.compile('电话：0\d{3}.\d+|联系方式：0\d{3}-\d+|电.*?话：0\d{3}-\d+')
        s2=re.compile('联系电话：.+\d+|联系方式：\d{11}|电话：\d{11}|手机：\d{11}')
        s3=re.compile('代理机构：.*?\n|代理机构：\n.*?\n|集中采购机构：\n.*?\n|招标代理：.*?\n')
        # s4=re.compile('联系事项：(.*?\n+.*?\n)')
        sa=re.findall(s0,i)
        saa=re.findall(s00,i)
        sb=re.findall(s1,i)
        st=re.findall(s2,i)
        sv=re.findall(s3,i)
        # sl=re.search(s4,i)
        if sa:
            # print sa[0]
            b1=sa[0].split('：')
            l.append(b1[1].decode('utf-8'))
        else:
            l.append('      ---')
        if sv:
            sv1=sv[0].split('：')
            l.append(sv1[1].decode('utf-8'))
        else:
            l.append('      ---')
        if saa:
            n=1
            for j in saa:
                # print j
                j1=j.split('：')
                if n>2:
                    continue
                l.append(j1[1].decode('utf-8'))
                n+=1
        else:
            l.append('      ---')
        if sb:
            sb1=sb[0].split('：')
            l.append(sb1[1].decode('utf-8'))
        else:
            l.append('      ---')
        if st:
            st1=st[0].split('：')
            l.append(st1[1].decode('utf-8'))
        else:
            l.append('      ---')

        # print '-'*15
        try:
            if sl.group(1):
                l.append(sl.group(1).encode('utf-8'))
            else:
                l.append('      ---')
        except:
            pass


        #print len(l)
        if len(l)<7:
            l.append('      ---')
        l.append(i.decode('utf-8'))
        lb.append(tuple(l))
        #print lb
    listname=['项目名称'.decode('utf-8'),'招标人/单位'.decode('utf-8'),'招标联系人'.decode('utf-8'),'代理人'.decode('utf-8'),'招标单位联系电话'.decode('utf-8'),'代理人联系电话'.decode('utf-8'),'代理机构'.decode('utf-8'),'全部信息'.decode('utf-8')]
    ppd=pd.DataFrame(lb,columns = listname)
    ppd.to_excel(r'D:\yinghao\%s.xls'%filename,encoding='utf-8')
if __name__=="__main__":
    filename=raw_input('请输入需要整理的文件名')
    write_into_excel(filename)
