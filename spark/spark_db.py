#! /usr/bin/env python
# coding:utf-8
# --------------------------------
# Created by coco  on 2017/8/1
# ---------------------------------
# Comment: 主要功能说明  连接spark master测试

from pyspark import SparkContext,SparkConf
from pyspark.sql.readwriter import DataFrameReader


# conf=SparkConf()
# conf.setMaster("spark://172.17.17.105:7077")
# conf.setAppName("test master connection")

#2个参数:   spark master   app name    "spark://172.17.17.105:7077","test master connection"
sc = SparkContext(appName="test master connection")
sql_sc = SQLContext(sc)
test_file_name = "/data/test_data/20170220/part-00000"

textFile = sql_sc.textFile("file:///data/test_data/20170220/part-00000")

print textFile.count()     # 打印文件的记录数
print textFile.first()

linesWithSpark = textFile.filter(lambda line:"Spark" in line)
linesWithSpark = textFile.filter(lambda line:"ppc" in line)