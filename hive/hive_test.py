#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/20
# ---------------------------------
# Comment: 主要功能说明

# table1: login_log
# card_acct	in_time	out_time
# anjingfeng	2017/7/14 17:15	2017/7/14 18:43
# anjingfeng	2017/7/14 14:37	2017/7/14 17:11
# anjingfeng	2017/7/14 12:24	2017/7/14 14:35
# anjingfeng	2017/7/14 11:11
# anjingfeng	2017/7/14 09:41	2017/7/14 11:08
# anjingfeng		2017/7/14 09:28
# anjingfeng	2017/7/14 08:26	2017/7/14 08:51
#
# # table2: oper_log
# mainacct	oper_time
# anjingfeng	2017/7/14 14:39
# anjingfeng	2017/7/14 16:39
# anjingfeng	2017/7/14 11:13

import time,datetime
import MySQLdb



# 时间转换函数:把一个字符串 转换为时间 datetime类型
def truns_time(t):
    # 这里根据情况时间格式可以自己调整:  "%Y/%m/%d %H:%M:"
    y,m,d,H,M=time.strptime("%s"%t, "%Y/%m/%d %H:%M")[0:5]
    t1=datetime.datetime(y,m,d,H,M)
    t1=int(time.mktime(t1.timetuple()))
    # print "打印时间t1:  "+str(t1)
    return t1



con_mysql = MySQLdb.Connection(host='192.168.8.94',user='mha_user',passwd='gc895316',db='wwn')

# 获取操作记录oper_log表中的记录
def  get_oper_info(oper_name):
    cursor = con_mysql.cursor()
    sql = "select oper_name,oper_time from oper_log where oper_name=%s"
    cursor.execute(sql,(oper_name,))
    oper_info_data = cursor.fetchall()
    return oper_info_data

# 获取门禁记录login_log表中的记录
def  get_login_info(oper_name):
    cursor = con_mysql.cursor()
    sql = "select login_name,in_time,out_time from login_log where login_name=%s"
    cursor.execute(sql,(oper_name,))
    login_info_data = cursor.fetchall()
    return login_info_data



if __name__ == '__main__':
    oper_name='anjingfeng'
    oper_user = get_oper_info(oper_name)

    for i in oper_user:
        print "##",i
        oper_name = i[0]
        oper_time =  i[1]
        op_time = truns_time(oper_time)

        login_user = get_login_info(oper_name)
        for j in login_user:
            login_list=[]
            in_time = j[1]
            out_time = j[2]
            # print in_time,out_time,oper_time
            if len(in_time)==0 or len(out_time)==0:
                pass
            else:
                i_time = truns_time(in_time)
                o_time = truns_time(out_time)
                # 判断如果oper_time在i_time,o_time之间 则返回 OK, 否则返回 异常
                if i_time <= op_time <= o_time:

                    login_list.append(j)
                    print oper_name +"\t" + str(oper_time) + "\t" +"OK"
                    print "登录的门禁记录为: " + str(in_time) +" \t " + str(out_time)
                    break

        if len(login_list)==0:
            print oper_name +"\t" + str(oper_time) + "\t" +"异常记录!"



