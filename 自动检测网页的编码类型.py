#!usr/bin/env python
# coding=utf-8
# author qzhn
# e-mail qzhn@163.com
import os
import sys
import chardet  # 字符集检测(编码检测)
from urllib import request

url = "http://blog.csdn.net/jsqfengbao/article/details/44591847"

def automatic_detect(url):
    content = request.urlopen(url).read()
    result = chardet.detect(content)#返回的是一个字典{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
    charset = result['encoding']  #取字典’encoding'所代表的值
    print (charset)
    mm=content.decode(charset)
    # print (mm)
    return charset

aa=automatic_detect(url)
print (aa)