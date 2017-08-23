#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/27
# ---------------------------------
# Comment: 主要功能说明   多进程

from multiprocessing import Pool
import  time

def test(x):
    print " 开始时间:" , x ,time.time()
    time.sleep(x)
    print " 结束时间: " , x ,time.time()

pool = Pool(2)
pool.map(test,(10,20,30))
pool.close() #清理掉进程池所有子进程。
while True:
    time.sleep(1)

# 清理掉进程池所有的子进程
pool.close()

