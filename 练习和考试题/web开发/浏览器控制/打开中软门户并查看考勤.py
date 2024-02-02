from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,pyinputplus,os.path,re,pyperclip,logging
from webdriver_manager.chrome import ChromeDriverManager
#不用下载drive的办法webdriver_manager


def intro(path):
    p='''运行此程序将自动打开门户网站并登录。打开个人考勤界面\n用户名密码为门户的账号密码\n考勤数据将保存在 %s 路径中'''%(path)
    return  print(p)
def userinput():
    user=pyinputplus.inputInt('请输入用户名:')
    userpass=input('请输入密码:')
    return str(user),str(userpass)

def senduser(drive,user,userpass,title):
    try:
        drive.find_element(By.NAME,'userName').click()
        drive.find_element(By.NAME,'userName').clear()
        drive.find_element(By.NAME,'userName').send_keys(user)
        time.sleep(1)

        drive.find_element(By.CSS_SELECTOR, '#password').click()
        drive.find_element(By.CSS_SELECTOR, '#password').clear()
        drive.find_element(By.CSS_SELECTOR, '#password').send_keys(userpass)
        time.sleep(1)

        button = drive.find_element(By.CSS_SELECTOR, '#dl > input.button')
        button.click()

    except NoSuchElementException:
        #如果元素找不到的异常，检查页面是否已经在下一页title中,是则表示页面已经跳转，元素找不到的异常可忽略。
        if drive.title==title:
            pass


def brower(user,userpass):
    opt = Options()
    opt.add_experimental_option('detach', True)
    #浏览器保持开启，除非最后close或者quit

    #opt.add_argument("--headless")
    #浏览器隐藏

    drive = webdriver.Chrome(options=opt, service=ChromeService(ChromeDriverManager().install()))
    # 不用下载drive的办法webdriver_manager

    drive.minimize_window()
    #设置浏览器大小drive.maximize_window()
    #drive.set_window_size()

    drive.implicitly_wait(5)
    #隐形等待，查询元素等待最多，5秒后timeout找不到元素
    drive.get('https://ics.chinasoftinc.com/SignOnServlet')
    WebDriverWait(drive,10).until(EC.title_is('中软国际门户系统'),'打开网址失败，请检查网络是否有问题')
    #显性等待，等到到结果出现为止


    for i in range(3):
        senduser(drive,user,userpass,title='chinasoft内部门户')
        #调用用户名密码输入函数并点击登录
        title = drive.title
        if title=='chinasoft内部门户':
            break
        else:
            assert drive.find_element(By.ID,'errorBox').is_displayed() is False ,'密码错误'
            # 如果页面没有跳转到正确的title先判断是否是密码错误，errorbox展示则意味着用户密码错误抛出异常停止程序
            #如果没有抛出异常，则刷新浏览器重试
            drive.refresh()
            #重试三次，防止页面卡顿点击登录失效的情况。每次重试重新输入用户名和密码，并点击登录
            continue
    #登录按钮需要设计一个自动重试功能


    WebDriverWait(drive, 10).until(EC.title_is('chinasoft内部门户'), '登录失败，页面没有打开')
    drive.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/a[4]').click()
    #个人考勤

    drive.switch_to.window(drive.window_handles[-1])
    #指向新打开的页签
    WebDriverWait(drive, 20).until(EC.title_is('员工端首页'),'页面没有打开员工端')

    drive.find_element(By.CSS_SELECTOR, 'body > div.app > div >\
         div.main_right.main_right_lf_none > div > div > div.right_box > div.content_menulist > div:nth-child(1)').click()
    #我的考勤
    WebDriverWait(drive, 10).until(EC.title_is('日考勤详情页面'),'页面没有打开日考勤详情页面')

    drive.find_element(By.CSS_SELECTOR, 'body > div.app > div > \
    div.main_right > div > div.content.layui-form.flex.row > div.leftcontent > div.rilitop > div.seedaka').click()
    #查看打卡记录
    WebDriverWait(drive, 10).until(EC.title_is('查看打卡数据'),'页面没有打开查看打卡记录')

    drive.find_element(By.CSS_SELECTOR, '#layui-laypage-1 > span.layui-laypage-limits > select > option:nth-child(3)').click()
    #换成50页
    time.sleep(1)

    datas=drive.find_elements(By.CSS_SELECTOR,'.layui-table-cell.laytable-cell-1-0-4')
    #找到打卡时间的数据class 用CSS来查找，class中的空格用‘.’替换
    ls = []
    for data in datas:
        ls.append(data.text)
    drive.quit()
    #关闭浏览器
    return ls

def main():
    path = os.getcwd()
    intro(path)
    user,userpass=userinput()
    assert len(user)>=6,'用户名格式不对'
    ls=brower(user,userpass)
    relo=re.compile(r'^(\d\d\d\d)-(\d\d).*$')
    #正则表达式2014-12
    date=relo.search(ls[1])
    #ls[0]是打卡记录 ls[1] 才是符合格式的时间
    file_name=date.group(1)+date.group(2)+'考勤'+'.txt'
    #拼装文件名201412.txt
    path=os.path.join(path,file_name)
    f=open(path,'w+')
    f.seek(0)
    f.write('\n'.join(ls[1:]))
    f.seek(0)
    pyperclip.copy(f.read())
    f.close()
    print('剪切板中已自动复制内容')
    #列表按行写入文件
    time.sleep(5)


if __name__ == '__main__':
    main()