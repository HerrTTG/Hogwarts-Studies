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
    pytest.main()

