#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/8/22
# ---------------------------------
# Comment: 主要功能说明  每秒钟ping db113一次记录日志。
import os
import time,datetime
import socket

def get_ip():
    '''
    获取主机名和主机IP
    '''
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    return myname,myaddr

def ping_vip(host):
    '''ping 1次指定地址'''
    import subprocess,traceback, platform
    if platform.system()=='Windows':
        cmd = 'ping -n %d %s'%(1,host)
    else:
        cmd = 'ping -c %d %s'%(1,host)
    try:
        p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (stdoutput,erroutput) = p.communicate()
        print stdoutput
    except Exception, e:
        traceback.print_exc()
    if platform.system()=='Windows':
        return stdoutput.find('Received = 1')>=0
    else:
        print   stdoutput.find('1 packets received')
        return stdoutput.find('1 packets received')>=0



if __name__ == '__main__':
    host = '192.168.0.111'
    #host = get_ip()[0]
    start_time = int(time.time())
    log_file = open('ping_ip.log','a')
    mess_time = "\n"+"开始执行时间:。。。。。" +str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    log_file.write(mess_time)
    if ping_vip(host) == True:
        rs_ip = get_ip()[1]
        mess = "\n" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') ) +"    访问的真实的IP: "+ rs_ip + "耗时: " +  str(int(time.time())-start_time)
        print mess
        log_file.write(mess)
    else:
        mess = "\n"+ "ping vip 失败!!!! 时间: " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print mess
        log_file.write(mess)



