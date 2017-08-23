#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/7/20
# ---------------------------------
# Comment: 主要功能说明
import sys
reload(sys)
# sys.getdefaultencoding('utf8')

import datetime


from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello django")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)