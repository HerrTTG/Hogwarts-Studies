@echo off
setlocal enabledelayedexpansion

set "chrome_path="
::从注册表查找谷歌浏览器路径
set reg_query_command=reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" /ve

::遍历注册表查询结果
for /f "tokens=2*" %%A in ('%reg_query_command%') do (
    ::如果有REG_SZ，则证明找到了谷歌浏览器
    if "%%A"=="REG_SZ" (
        ::如果路径存在，则设置谷歌浏览器绝对路径到变量chrome_path
        set "tmp_chrome_path=%%B"
        if exist "!tmp_chrome_path!" (
            set "chrome_path=%%B"
        )
    )
)

::如果上面找到了谷歌浏览器的路径
if defined chrome_path (
    ::打印找到了谷歌浏览器的文件地址
    echo Chrome found at: "%chrome_path%"
    ::带参启动谷歌浏览器，使其不校验跨域问题 （./表示当前目录， 可以修改为你所需要的工作目录）
    "%chrome_path%" --disable-web-security --user-data-dir="%~dp0/tmp" "%~dp0/index.html"
) else (
    ::如果没找到，打印没找到
    echo Chrome not found.
    ::打印启动web信息
    echo start a webserver ...
    ::启动一个web服务监听5001端口，在后台运行。默认用当前文件夹的index.html作为首页
    start /b http_server.exe -port 5001
    ::使用默认浏览器打开web服务的地址并等待浏览器关闭
    start "" /WAIT http://127.0.0.1:5001
)
