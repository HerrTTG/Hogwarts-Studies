from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

option = Options()
option.debugger_address = 'localhost:9222'

driver = webdriver.Chrome(options=option)

for i in driver.find_elements(By.CSS_SELECTOR,
                              ".qui_dialog.ww_dialog.qui_dialog.ww_dialog.ww_dialog_NoWidthLimit.multiselect_dialog.hidden_checkbox"):
    if i.is_displayed():
        ele = i
    else:
        ele = False
else:
    assert ele
