#!usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="wanglu_test",port=3306,charset="utf8")
cur=conn.cursor()
