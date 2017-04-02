#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:37:04 2017

@author: yjt
"""
#! -*- coding:utf-8 -*-
import jieba
import json
import codecs

with open('Fight.json', 'r') as f:
 data = json.load(f,encoding="UTF-8")

seg_list = jieba.cut(data[:-1]['DocContent'], cut_all = True)
#print "Full Mode:", ' '.join(seg_list)


tf={}
for seg in seg_list :
  #  print '1' + seg
    seg = ''.join(seg.split())
    if (seg != '' and seg != "\n" and seg != "\n\n") :
        if seg in tf :
            tf[seg] += 1
        else :
            tf[seg] = 1

f = codecs.open("result.txt","w+",'utf-8')
for item in tf:
    #print item
    f.write(item+"  "+str(tf[item]).encode('gb2312')+"\n")
f.close()

