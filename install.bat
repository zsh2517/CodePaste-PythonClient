@echo off
echo 请稍等正在检测UAC权限
rd C:\windows\testuac >nul 2>nul
mkdir C:\windows\testuac 1>nul 2>nul
set /a err=%errorlevel%
if "%err%" == "1" (
    echo 需要UAC权限才能运行
    echo 请重新以管理员权限运行
    echo 按任意键退出
    pause>nul
    exit
)
rd C:\windows\testuac >nul 2>nul
echo 本程序正在以UAC权限运行
echo.
echo codepaste环境安装
echo ver2.0
echo.
echo 0. 安装依赖库
echo 1. 安装环境
echo 2. 删除环境
echo 9. 删除旧版环境
set /p choice=请输入:
goto menu%choice%
:menu0
echo 根据自己情况直接复制安装即可
echo 使用到了以下库
echo.
echo os
echo requests
echo json
echo html
echo pyperclip
echo chardet
echo.
echo pip install os
echo pip install requests
echo pip install json
echo pip install html
echo pip install pyperclip
echo pip install chardet
echo.
echo pip3 install os
echo pip3 install requests
echo pip3 install json
echo pip3 install html
echo pip3 install pyperclip
echo pip3 install chardet
echo.
echo 安装完成之后任意键继续即可
pause>nul
:menu1
echo 如果不能拖动请粘贴
REM set /p pyexe=请拖入python3的可执行程序
set pyexe=C:\Program Files\Python38\python.exe
set /p pyprogram=请拖入Paste.py
echo y|reg add HKEY_CLASSES_ROOT\.codepaste /ve /d ".Paste codepaste File"
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /ve
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /v Command /d "\"%pyexe%\" \"%pyprogram%\" -g -q -f \"%%1\""
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /v FileNull
echo 由于程序不能创建快捷方式，请根据下列介绍手动创建
echo 正在打开目录%appdata%\Microsoft\Windows\SendTo
start "" "%appdata%\Microsoft\Windows\SendTo"
echo 请复制下面的东西，然后新建一个快捷方式
echo ^"%pyexe%^" ^"%pyprogram%^" -s -q -f
echo 文件名写发送到Paste之类的东西
REM "C:\Program Files\Python38\python.exe" C:\Users\zsh2517\project\codepaste\Paste.py -pauto
pause
exit
:menu2
echo yes | reg delete HKCR\.codepaste
pause
exit
:menu9
REM echo reg delete HKCR\.CodePastt
echo yes | reg delete HKCR\.CodePastt
REM echo reg delete HKCR\.codepaste
echo yes | reg delete HKCR\.codepaste
pause