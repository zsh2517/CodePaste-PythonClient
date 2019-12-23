# -*- coding: UTF-8 -*-
# MSDN windows API
# https://docs.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#completing-verb-implementation-tasks
import sys
import os
import requests
import json
import html
import pyperclip
import chardet

import Config

def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']
def PasteDirect(filepath):
    # print(filepath)
    temp1=filepath.split("\\")
    temp2=temp1[len(temp1)-1].split(".")
    temp3=get_encoding(filepath)
    file=open(filepath,encoding=temp3)
    ret={
        "title": temp1[len(temp1)-1],
        "language":temp2[len(temp2)-1],
        "author":Config.username,
        "expiration":"-1",
        "password":"",
        "encoding":temp3,
        "api":"python",
        "code":html.escape(file.read())
    }
    file.close()
    # print(ret)
    return ret
def PasteClipboard():
    ret={
        "title": "clipboard",
        "language":"",
        "author":Config.username,
        "expiration":"-1",
        "password":"",
        "encoding":"utf-8",
        "api":"python",
        "code":html.escape(pyperclip.paste())
    }
    return ret
def query(ret):
    # print("QQWQQ")
    print("请输入作者(缺省：%s)"%(ret["author"]))
    temp=input()
    if temp!="":
        ret["author"]=temp
    print("请输入过期时间(缺省：%s(永久))"%(ret["expiration"]))
    temp=input()
    if temp!="":
        ret["expiration"]=temp
    print("请输入访问密码(缺省：无密码)")
    temp=input()
    if temp!="":
        ret["password"]=temp
    print("请输入语言(缺省：%s)"%(ret["language"]))
    temp=input()
    if temp!="":
        ret["language"]=temp
    print("请输入文件名(缺省：%s)"%(ret["title"]))
    temp=input()
    if temp!="":
        ret["title"]=temp
    # print(ret)
    return ret
def PasteQuery(filepath):
    ret=PasteDirect(filepath)
    query(ret)
    return ret
def PasteIt(ret):
    url=Config.url
    url_proc=url+"proc.php"
    # print(url_proc)
    response=requests.post(url=url_proc)
    # print(url_proc)
    response=requests.post(url=url_proc,data=ret)
    print(response.text)
    print(url+"paste.php?id="+response.text)
    pyperclip.copy(url+"paste.php?id="+response.text)
    os.system("pause")
    exit(0) 
