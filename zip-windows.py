#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 使用方式 python zip-windows.py /Users/Yesoul/Downloads/体脂秤.zip

import os
import sys
import zipfile

reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.getdefaultencoding()
#print "Processing File" + sys.argv[1]
query='0' ## 是否成功的标志
path=sys.argv[1] ## 获取路径
try:
    file = zipfile.ZipFile(path, "r");
except IOError:
    sys.stdout.write(query) ## 异常捕捉, 如果不是正当的路径, 方便 Alfred 拿到是否成功的标志
for name in file.namelist():
    utf8name = name.decode("gbk")
    #print "Extracting " + utf8name
    
#  原本用字符串分割, 拼接解决路径问题, 写完了以后发现傻逼了... 一句os.path.dirname 就可以直接拿到文件所在目录
#    pathnameArr = path.split('/')
#    pathnameArr.pop(0)
#    pathnameArr.pop(-1)
#    pathname = '/'+'/'.join(pathnameArr)+'/'+utf8name
#    utf8name = '/'+'/'.join(pathnameArr)+'/'+utf8name

    # 这是要解压的文件所在的文件夹
    # eg. /Users/Yesoul/Downloads/1.png 变成 /Users/Yesoul/Downloads/
    # os.path.dirname 直接拿到文件夹路径
    pathname = os.path.dirname(os.path.dirname(path)+'/'+utf8name)
    # 要解压的文件内容路径
    # eg. /Users/Yesoul/Downloads/1.png
    utf8name = os.path.dirname(path)+'/'+utf8name
    
    # 判断是否文件夹存在, 不存在就创建
    if not os.path.exists(pathname) and pathname != "":
        os.makedirs(pathname)
    
    # 读取文件内容
    data = file.read(name)

    # 判断文件夹内是否有该内容, 没有就写入文件内容并将成功标志赋值1
    if not os.path.exists(utf8name):
        fo = open(utf8name, "w")
        fo.write(data)
        fo.close
        query='1'
file.close
# 输出成功标志, 给予 Alfred 使用
sys.stdout.write(query)
