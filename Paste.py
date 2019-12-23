# -*- coding: UTF-8 -*-
# https://docs.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#completing-verb-implementation-tasks
import sys
# import os
import SendToPaste
import GetFromPaste
import argparse
import os
args = argparse.ArgumentParser()
group = args.add_mutually_exclusive_group()
group.add_argument("-s","--send",help="设定为发送",action="store_true")
group.add_argument("-g","--get",help="设定为接收",action="store_true")
biggroup=args.add_mutually_exclusive_group()
biggroup.add_argument("-d","--direct",help="直接",action="store_true")
biggroup.add_argument("-q","--query",help="询问",action="store_true")
group2=args.add_mutually_exclusive_group()
group2.add_argument("-cu","--clipURL",help="从剪贴板获取URL",action="store_true")
group2.add_argument("-u","--url",help="指定URL/ID")
group3=args.add_mutually_exclusive_group()
group3.add_argument("-f","--file",help="指定文件操作")
group3.add_argument("-cc","--clipCode",help="使用剪贴板",action="store_true")

arg = args.parse_args()
print(arg)
# os.system("pause")
if arg.send:
    if arg.clipCode:
            # paste -s -cc
            # paste -s -d -cc
            ret=SendToPaste.PasteClipboard()
            if arg.query:
                # paste -s -q -cc
                ret=SendToPaste.query(ret)
    else:
        if arg.direct:
            # paste -s -d -f FILE
            ret=SendToPaste.PasteDirect(arg.file)
        else:
            # paste -s -q -f FILE
            ret=SendToPaste.PasteQuery(arg.file)
    SendToPaste.PasteIt(ret)
elif arg.get:
    # # arg.query
    # if arg.clipURL:
    #     # paste -g -cu 
    #     if arg.clipCode:
    #         # paste -g -cu -cc
    #     else:
    #         if arg.direct:
    #         # paste -g -d -cu -f -FILE
    #         else:
    #         # -paste -g -q -cu -f FILE
    URL=""
    if arg.clipURL:
        # paste -g -cu
        URL=GetFromPaste.getclipurl()
    else:
        # paste -g -u URL
        URL=arg.url
    if URL=="" or URL==None or arg.query:
        # 未指定
        URL=GetFromPaste.geturl()
    URL=GetFromPaste.formaturl(URL)
    ret=GetFromPaste.getret(URL)
    if arg.clipCode:
        #paste -g [u] -cc
        GetFromPaste.PasteClipboard(ret)
        exit(0)
    else:
        if arg.file!=None and (arg.query==False or arg.direct==True):
            # paste -g [u] -f FILE
            f=GetFromPaste.GetSamePath(arg.file,ret)
            print(f)
            # 写出到文件
        else:
            # paste -g [u] -q 或者paste -g [u] 
            print("请输入要保存到的文件 默认"+ret["title"])
            fff=input()
            if fff=="":
                fff=ret["title"]
            if arg.file[-9:]=="codepaste":
                f=""
                ff=arg.file.split("\\")
                for index in range(len(ff)-1):
                    f=f+ff[index]+"\\"
                # print(ret)
                f=f+fff
            # 写出到文件 
        print("写出到"+f)
        GetFromPaste.writetofile(f,ret)
        os.system("pause")