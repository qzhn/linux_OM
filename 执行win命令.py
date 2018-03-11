#!usr/bin/env python
# coding=utf-8
import os
import sys


b=os.popen('ping 192.168.1.1')
print (b.read())
#        read 后面一定要加括号