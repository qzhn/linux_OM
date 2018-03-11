#!usr/bin/env python
# coding=utf-8
import os
import sys
a=input('请输入目录：')
d=os.popen ("dir {}".format(a))
f= (d.read())
print (f)
print (len(f))
g=input('请输入查找的关键字')
print(g)
e=f.find(g)
print (e)
h=len(g)
print (f[:(e+h)])