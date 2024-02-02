from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

opt = Options()
opt.add_experimental_option('detach', True)

brower = webdriver.Chrome(options=opt, service=ChromeService(ChromeDriverManager().install()))
brower.get('https://tieba.baidu.com/')

serchElem = brower.find_element(By.NAME, 'kw1').send_keys('DNF')
submitElem = brower.find_element(By.CSS_SELECTOR,
                                 '#tb_header_search_form > span.search_btn_wrap.search_btn_enter_ba_wrap > a').click()
