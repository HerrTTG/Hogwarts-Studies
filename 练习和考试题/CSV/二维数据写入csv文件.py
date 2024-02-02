ls=[['GROUP_CODE', 'GROUP_NAME', 'PRI_IDENTITY', 'EFF_DATE', 'EXP_DATE'], ['1', 'BULK_SHOP', '7484603', '2012-09-30 09:40:46', '2037-01-01 00:00:00'], ['1', 'BULK_SHOP', '7570348', '2012-09-30 09:38:57', '2037-01-01 00:00:00'], ['1', 'BULK_SHOP', '7470795', '2012-09-30 09:45:03', '2037-01-01 00:00:00'], ['1', 'BULK_SHOP', '7475750', '2012-09-30 09:26:55', '2037-01-01 00:00:00']]


fw=open("/练习和考试题/文本处理/写入2.csv", "w", encoding='utf-8')


for i in ls:
    #i此时是一维列表，join(i)取列表i中的每一个元素在加上逗号，即'GROUP_CODE', 'GROUP_NAME', 'PRI_IDENTITY', 'EFF_DATE', 'EXP_DATE'
    #print(lns)
    fw.write(",".join(i)+"\n")