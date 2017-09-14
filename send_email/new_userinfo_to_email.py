#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/9/9
# ---------------------------------
# Comment: 主要功能说明
# 监控到新注册用户,发邮件给相关人的邮箱。
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyh import *
import MySQLdb
import time,datetime,os
import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# qq邮箱授权码
_pwd='zpgflkiksbxibggf'

global conn_mysql
conn_mysql = MySQLdb.connect(host='118.89.220.36',user='mha_user',passwd='gc895316',db='bx_abc')

def get_userinfo(sql):
    cur = conn_mysql.cursor()
    cur.execute(sql)
    rs = cur.fetchall()
    return rs

# 获取本月第一天的时间戳
def get_month_timestamp():
    NowYear = time.localtime()[0]
    NowMonth = time.localtime()[1]
    # LastMonth = NowMonth - 1
    # if NowMonth == 1:
    #     LastMonth = 12
    #     NowYear = NowYear -1
    result = "%s-%s-%d" % (NowYear, NowMonth, 1)
    TimeStamp=time.mktime(time.strptime(result,'%Y-%m-%d')) #日期转换为时间戳
    # LocalTime = time.localtime(TimeStamp)#将日期时间戳转换为localtime
    return   TimeStamp

# send email to users
def sendmail(msg):
    '''''
    @subject:邮件主题
    @msg:邮件内容
    @toaddrs:收信人的邮箱地址
    @fromaddr:发信人的邮箱地址
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com
    @password:发信人的邮箱密码
    '''
    fromaddr = "lantian_929@163.com"
    smtpaddr = "smtp.163.com"
    toaddrs = ["120890945@qq.com","943489924@qq.com","271728979@qq.com","505972916@qq.com","90579323@qq.com","287112491@qq.com","136177121@qq.com","517056585@qq.com"]
    subject = "恭喜您,您有新用户注册。。。"
    password = "lantian929?"

    mail_msg = MIMEMultipart()
    if not isinstance(subject,unicode):
        subject = unicode(subject, 'utf-8')
    mail_msg['Subject'] = subject
    mail_msg['From'] =fromaddr
    mail_msg['To'] = ','.join(toaddrs)
    mail_alternative = MIMEMultipart('alternative')
    mail_msg.attach(mail_alternative)
    # html格式
    mail_alternative.attach(MIMEText(msg, 'html', 'utf-8'))

    try:
        s = smtplib.SMTP()
        s.connect(smtpaddr)  #连接smtp服务器
        s.login(fromaddr,password)  #登录邮箱
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件
        s.quit()
    except Exception,e:
       print "Error: unable to send email"
       print traceback.format_exc()

# 结果转化成html
def to_html(new_userinfo,month_userinfo):
    page = PyH('new mail')
    page<<div(style="text-align:left")<<h4('HI:all  congratulation!!!!     you have a new user sign in.')
    page<<div(style="text-align:center")<<h4('The total information')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr3 = mytab << tr(bgcolor="lightgrey")
    tr3 << th('month_count') + th('total_count')
    for m in range(len(month_userinfo)):
        tr4 = mytab << tr()
        for n in range(2):
            tr4 << td(month_userinfo[m][n])

    page<<div(style="text-align:center")<<h4('new user info')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('uid') + th('username')+th('real_name') +th('phone') + th('wechat') +th('addtime')
    for i in range(len(new_userinfo)):
        tr2 = mytab << tr()
        for j in range(6):
            tr2 << td(new_userinfo[i][j])
            if new_userinfo[i][j]=='':
                tr2[1].attributes['style']='color:red'
    page.printOut('test.html')


if __name__ == '__main__':

    # 查询有新用户注册则发邮件,否则pass
    max_uid = get_userinfo(sql='select max(uid) from bx_user')[0]
    print "max_uid = " + str(max_uid)

    # 获取mark_uid.txt文件中的标记uid
    with open('mark_uid.txt','r') as f:
        mark_uid = f.readlines()[-1]
        f.close()
    print mark_uid
    if mark_uid < max_uid:
        userinfo = get_userinfo(sql='select uid,username,real_name,phone,qq,email,weixin,addtime from bx_user where uid>%s'%mark_uid)
        user_count = len(userinfo)

        if user_count>0:
            new_userinfo_list = []
            for i in userinfo:
                uid = i[0]
                username = i[1]
                real_name = i[2]
                phone = i[3]
                weixin = i[6]
                addtime = i[7]
                # 转换addtime为时间格式
                addtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(addtime))
                # new_userinfo = {"uid":uid,"username":username,"real_name":real_name,"phone":phone,"weixin":weixin,"addtime":addtime}
                new_userinfo = [uid,username,real_name,phone,weixin,addtime]
                new_userinfo_list.append(new_userinfo)
            mark_uid = uid

            print new_userinfo_list

            # 记录mark_uid
            f = open('mark_uid.txt','a')
            f.write(str(mark_uid)+'\n')
            f.close()

            # 当月新增用户数量
            # 获取本月第一天的时间戳
            month_time = int(get_month_timestamp())
            print month_time
            user_count_month = get_userinfo(sql = ' select count(*) from bx_user where addtime>=%s '%month_time)[0]
            print "本月用户数量为: " + str(user_count_month[0])
            # 总计用户数
            user_total = get_userinfo(sql = 'select count(*) from bx_user where uid>3000 ')[0]
            print "总用户数量为: " + str(user_total)

            month_userinfo_list = [[user_count_month[0],user_total[0]]]
            print    month_userinfo_list

            htmlText = open('test.html').read()

            print htmlText
            print type(htmlText)

            msg = htmlText
            sendmail(msg)

        else:
            print "没有新用户注册."
            pass











