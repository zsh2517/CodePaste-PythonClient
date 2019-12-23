import requests
import pyperclip
import html
import os
import json

import Config

def geturl(): # 用户输入URL
    print("请粘贴地址或id")
    inputid=input()
    return formaturl(inputid)
def getclipurl(): # 读取剪贴板URL
    inputid=pyperclip.paste()
    return formaturl(inputid)
def formaturl(url): # URL格式化
    if url[0:4]=="http":
        lines=url.split("=")
        url=lines[len(lines)-1]
    return Config.url+"paste.php?access=api&id="+url
def getret(url): # 返回ret
    ret=requests.post(url)
    while ret.text[0]=="1":
        print("请输入密码")
        password=input()
        ret = requests.post(url,data={"password":password})
    if(ret.text[0]=="3"):
        print("内容已过期，无法查看，任意键关闭")
        os.system("pause>nul")
        exit(0)
    ret=ret.text[1:]
    # print("\n")
    # print(ret)
    ret=json.loads(ret)
    return ret

def PasteClipboard(ret): # 粘贴代码
    # print(html.unescape(ret["code"]))
    pyperclip.copy(html.unescape(ret["code"]))
# def writetofile(filepath, ret):

def GetSamePath(filepath, ret): 
    # 如果指定的是一个codepaste（新建）文件，那么采用则采用指定的函数
    # 否则直接写出
    if filepath[-9:]=="codepaste":
        f=""
        ff=filepath.split("\\")
        for index in range(len(ff)-1):
            f=f+ff[index]+"\\"
        # print(ret)
        f=f+ret["title"]
        return f
    else:
        return filepath
def writetofile(filepath,ret):
    # print("success")
    file=open(filepath,"w")
    code=html.unescape(ret["code"])
    code=code.replace("\r\n","\n")
    file.write(code)
    file.close()

# if "title" not in ret: # BUG
#     ret["title"]="Untitled."+ret["language"]
# print("请输入文件名(默认%s)"%(ret["title"]))
# filename=input()
# if filename=="":
#     filename=ret["title"]
# # exit(0)
# file_dir=cmd[2].split("\\" )
# dir=""
# for index in range(len(file_dir)-1):
#     dir=dir+file_dir[index]+"/"
# os.rename(cmd[2],dir+filename)
