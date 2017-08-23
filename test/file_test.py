#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/21
# ---------------------------------
# Comment: 主要功能说明

# import os

try:
    filename=raw_input("Enter your file name :    ")

    fobj = open(filename,'r')

    for eachLine in fobj:
        print eachLine ,
    fobj.close()
except IOError, e:
    print "file open error :", e



def addMysel(x):
    'apply + operation to argment'
    return x+x

print addMysel(x='ab')
print addMysel(x=1)

class myclass(object):
