from selenium import webdriver

##步骤一，配置chrome浏览器的程序路径到系统变量中的path上
##步骤二，关闭所有浏览器进程。使用命令行打开浏览器
# chrome --remote-debugging-port=9222
# 步骤三，代码中设置配置
option = webdriver.ChromeOptions()
option.debugger_address = "localhost:9222"

# 步骤四，drvier实例化时传入配置
driver = webdriver.Chrome(options=option)
driver.get("https://work.weixin.qq.com/wework_admin/frame")

# 复用浏览器常用于需要人为干预的操作的自动化场景
# 如企业微信https://work.weixin.qq.com/wework_admin/frame 需要扫码登录
# 如果不使用浏览器复用，每次driver都会启动新的浏览器。新浏览器不会存在cookie信息等鉴权信息。
# 而浏览器复用就可以先人为操作，使鉴权信息保留在浏览器中。在直接调用此浏览器进行自动化。
# 只要浏览器不关闭，信息就可继承