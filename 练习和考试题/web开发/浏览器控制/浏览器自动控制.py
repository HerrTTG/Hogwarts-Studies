from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,sys,threading
from tqdm import tqdm



def brower():
    opt = Options()
    opt.add_experimental_option('detach', True)
    #设置页面保持打开除非close不关闭浏览器
    brower = webdriver.Chrome(options=opt,service=ChromeService(ChromeDriverManager().install()))

    brower.get('http://www.baidu.com')
    time.sleep(2)
    try:
        tibaElem=brower.find_element(By.CSS_SELECTOR,'#s-top-left > a:nth-child(4)').click()
        #寻找元素并点击
    except:
        print('打开%s失败' %(tibaElem))
        sys.exit(1)
    else:
        time.sleep(2)
        #等待页面加载，并切换到最新窗口
        brower.switch_to.window(brower.window_handles[-1])

    try:
        serchElem=brower.find_element(By.NAME,'kw1').send_keys('DNF')
        submitElem=brower.find_element(By.CSS_SELECTOR,'#tb_header_search_form > span.search_btn_wrap.search_btn_enter_ba_wrap > a').click()
    except:
        print('输入内容失败，或者submit失败')
        sys.exit(1)
    else:

        time.sleep(2)
        # 等待新页面加载
        htmlElem = brower.find_element(By.TAG_NAME, 'html')
        #对象为整个页面
        htmlElem.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        htmlElem.send_keys(Keys.PAGE_DOWN)
        #进行页面下滚动

def process():
    iterable = range(100)
    for i in tqdm(iterable):
        pass

def main():
    p1=threading.Thread(target=brower())
    p2 = threading.Thread(target=process())
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()