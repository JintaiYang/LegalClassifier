#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:21:55 2017

@author: yjt
"""

# coding=gbk
import codecs

f = codecs.open('intimate.txt','a','utf-8')
f.write(u'中文')
s = u'中文'
f.write(s)
f.close()

f = codecs.open('intimate.txt','r','utf-8')
s = f.readlines()
f.close()
for line in s:
    print line