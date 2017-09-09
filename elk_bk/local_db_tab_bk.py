#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/8/29
# ---------------------------------
# Comment: 主要功能说明
# 主要备份ELK数据库中被标记的相关表。

import os,datetime
import pg
import subprocess



global start_gds_cmd

# 检查服务是否存在,如果存在了pass不存在启动
def proc_exist(cmd):
    process = '/home/use/gds.lock'
    os.system('ps -ef |grep gds |grep -v grep >%s' % process)
    if not (os.path.getsize(process)) :
        print "启动gds进程。。。。。"
        os.system(cmd)
    else:
        print "gds进程已经启动。"
pgdb_conn = pg.connect(dbname = 'zybdb', host = '192.168.230.128', user = 'omm', passwd = '888888' ,port=25108)
def op_pg_db(sql):
    try:
        rs = pgdb_conn.query(sql).getresult()
    except Exception, e:
        print e.args[0]
        print "conntect postgre database failed, ret = %s" % e.args[0]
        pgdb_conn.close()
    return rs

# 基于备份系统创建外表 ,创建表之前要删除,删除完毕,然后再创建
def create_forign_tab():
    #拼装删除表sql,结果是一个 drop foreign table 集
    sql = ''' select .... '''
    # 循环执行drop表操作
    for i in op_pg_db(sql):
        try:
            op_pg_db(i)
        except Exception ,e:
            print 'drop  table failed  %s' %e.args[0]

    # 拼装创建表sql,结果是一个 create forign talbe 集
    sql = '''  select    '''
    # 循环执行 create表操作
    for j in op_pg_db(sql):
        try:
            op_pg_db(j)
        except Exception,e:
            print 'create table failed ...%s' %j


# 判断文件夹是否存在,不存在创建
def file_dir_exist(filename):
    is_path = '/home/use/%s'%filename + str(datetime.datetime.now().strftime('%Y%m%d'))
    if not os.path.exists(is_path):
        os.makedirs(is_path)
        print "创建文件夹:"  +is_path



if __name__ == '__main__':
    # 确定要备份的文件夹
    file_name = ['ODS','CRM','PMA','HDP','FTP']
    for i in file_name:
        filename = i
        file_dir_exist(filename)
    # drop && create
    create_forign_tab()

    # 开始备份,执行备份脚本 back_up.py
    INTERPRETER = "/usr/bin/python"
    processor = "md5get.py"
    pargs = [INTERPRETER, processor]
    pargs.extend(["--input=inputMd5s"])
    subprocess.Popen(pargs)




