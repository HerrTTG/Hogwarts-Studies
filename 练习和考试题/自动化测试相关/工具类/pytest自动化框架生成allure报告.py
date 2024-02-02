import pytest,openpyxl


wb=openpyxl.open('testing.xlsx')
sheet=wb['Sheet1']
all_case=[]
for obj in list(sheet.columns)[1]:
    if obj.value == 'Case Name':
        continue
    else:
        all_case.append(obj.value)

@pytest.mark.parametrize('case',all_case)
def test_case_exec(case):
    print(case)

if __name__=='__main__':
    pytest.main(['--alluredir=allure-resultes'])
    #生成allure报告存放在allure-resultes路径下
    #下一步 安装allure 用os.system执行allure 生成报告
    #os.system(r'allure generate -c -o 测试报告')

