dic_misiden = {}
read_handle = open('all_misiden.unl', 'r')
data_train = read_handle.readline().strip('\n')
while data_train:
    file_list = data_train.split('|')
    dic_misiden[file_list[0]] = 1
    data_train = read_handle.readline().strip('\n')
read_handle.close()

dic_segement = {}
read_handle = open('BP_MOBILE_SEG_ROUTER.unl', 'r')
data_train = read_handle.readline().strip('\n')
while data_train:
    file_list = data_train.split('|')
    if file_list[6] == "C":
        dic_segement[file_list[0]] = file_list[1]
    else:
        num_temp = 0
    data_train = read_handle.readline().strip('\n')
read_handle.close()

write_hanle = open("free_misisden.unl", "w")
for i in dic_segement:
    t = int(i)
    while t <= int(dic_segement[i]):
        if t >= int(i) and t <= int(dic_segement[i]):
            str_misiden = str(t)
            if str_misiden in dic_misiden:
                num_tem = 0
            else:
                write_hanle.write(str(t) + "\n")
            t = int(t) + 1
        else:
            t = t + 1
write_hanle.close()
