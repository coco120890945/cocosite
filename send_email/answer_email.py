#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/9/20
# ---------------------------------
# Comment: 主要功能说明: 有用户问问题是,及时通知
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

def do_op_db(sql):
    conn_mysql = MySQLdb.connect(host='118.89.220.36',user='mha_user',passwd='gc895316',db='bx_abc')
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
    toaddrs = ["120890945@qq.com"]
               # "943489924@qq.com",
               # "271728979@qq.com",
               # "505972916@qq.com",
               # "290579323@qq.com",
               # "287112491@qq.com",
               # "136177121@qq.com",
               # "517056585@qq.com"]
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
def to_html(ask_info_list,ask_total_info_list):
    page = PyH('new mail')
    page<<'<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    page<<'<font  >&nbsp;&nbsp;&nbsp;&nbsp;HI:all</font>'
    page<<div(style="text-align:left")<<h4('&nbsp;&nbsp;&nbsp;&nbsp; you have a new ask .')

    page<<div(style="text-align:center")<<h4('Ask total information')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr3 = mytab << tr(bgcolor="lightgrey")
    tr3 << th('ask_count_month') +th('ask_total')
    for i in range(len(ask_total_info_list)):
        tr4 = mytab << tr()
        for j in range(2):
            tr4 << td(ask_total_info_list[i][j])

    page<<div(style="text-align:center")<<h4('new ask info')
    mytab = page << table(border="1",cellpadding="3",cellspacing="0",style="margin:auto")
    tr1 = mytab << tr(bgcolor="lightgrey")
    tr1 << th('askid') + th('ask_title')+th('ask_content') +th('uid') + th('ask_time')
    for i in range(len(ask_info_list)):
        tr2 = mytab << tr()
        for j in range(5):
            tr2 << td(ask_info_list[i][j])
            if ask_info_list[i][j]==' ':
                tr2.attributes['bgcolor']='yellow'
            if ask_info_list[i][j]=='':
                tr2[1].attributes['style']='color:red'
    return page.printOut('ask.html')

if __name__ == '__main__':

    # 查询有新用户注册则发邮件,否则pass
    ask_max_timestamp = do_op_db(sql=' select max(ask_time) from bx_ask ')[0][0]
    print "ask_max_timestamp = " + str(ask_max_timestamp)


    # 获取mark_uid.txt文件中的标记uid
    with open('ask_max_timestamp.txt','r') as f:
        mark_time = f.readlines()[-1]
        f.close()
    print mark_time
    # mark_time = 1502788555
    if int(mark_time) < int(ask_max_timestamp):
        ask_info = do_op_db(sql='select askid,ask_title,ask_content,uid,ask_time from bx_ask where uid>3000 and ask_time>%d and mark=0 '%int(mark_time))

        if len(ask_info)>0:
            ask_info_list = []
            for i in ask_info:
                print i
                askid = i[0]
                ask_title = i[1]
                ask_content = i[2]
                uid = i[3]
                ask_time = i[4]
                # 转换addtime为时间格式
                ask_datetime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(ask_time))

                ask_info = [askid,ask_title,ask_content,uid,ask_datetime]
                ask_info_list.append(ask_info)

            mark_time = ask_time

            print ask_info_list

            # 记录mark_uid
            f = open('./ask_max_timestamp.txt','a')
            f.write(str(mark_time)+'\n')
            f.close()

            # 当月新增用户数量
            # 获取本月第一天的时间戳
            month_time = int(get_month_timestamp())
            print month_time
            ask_count_month = do_op_db(sql = ' select count(*) from bx_ask where uid>3000 and ask_time>%d and mark=0; '%month_time)[0]
            print "本月用户自主提问次数: " + str(ask_count_month[0])


            # 提问问题总数
            ask_total = do_op_db(sql = 'select count(*) from bx_ask where uid>3000 and mark=0;')[0]
            print "总用户数量为: " + str(ask_total[0])

            ask_total_info_list = [[ask_count_month[0],ask_total[0]]]
            print    ask_total_info_list

            to_html(ask_info_list,ask_total_info_list)

            htmlfile = open('ask.html')
            htmlText = htmlfile.read()

            print htmlText

            msg = htmlText
            sendmail(msg)
            htmlfile.close()

        else:
            print "没有自主用户提问新问题。。。。"
            pass


