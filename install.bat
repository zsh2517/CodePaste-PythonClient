@echo off
echo ���Ե����ڼ��UACȨ��
rd C:\windows\testuac >nul 2>nul
mkdir C:\windows\testuac 1>nul 2>nul
set /a err=%errorlevel%
if "%err%" == "1" (
    echo ��ҪUACȨ�޲�������
    echo �������Թ���ԱȨ������
    echo ��������˳�
    pause>nul
    exit
)
rd C:\windows\testuac >nul 2>nul
echo ������������UACȨ������
echo.
echo codepaste������װ
echo ver2.0
echo.
echo 0. ��װ������
echo 1. ��װ����
echo 2. ɾ������
echo 9. ɾ���ɰ滷��
set /p choice=������:
goto menu%choice%
:menu0
echo �����Լ����ֱ�Ӹ��ư�װ����
echo ʹ�õ������¿�
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
echo ��װ���֮���������������
pause>nul
:menu1
echo ��������϶���ճ��
REM set /p pyexe=������python3�Ŀ�ִ�г���
set pyexe=C:\Program Files\Python38\python.exe
set /p pyprogram=������Paste.py
echo y|reg add HKEY_CLASSES_ROOT\.codepaste /ve /d ".Paste codepaste File"
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /ve
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /v Command /d "\"%pyexe%\" \"%pyprogram%\" -g -q -f \"%%1\""
echo y|reg add HKEY_CLASSES_ROOT\.codepaste\ShellNew /v FileNull
echo ���ڳ����ܴ�����ݷ�ʽ����������н����ֶ�����
echo ���ڴ�Ŀ¼%appdata%\Microsoft\Windows\SendTo
start "" "%appdata%\Microsoft\Windows\SendTo"
echo �븴������Ķ�����Ȼ���½�һ����ݷ�ʽ
echo ^"%pyexe%^" ^"%pyprogram%^" -s -q -f
echo �ļ���д���͵�Paste֮��Ķ���
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