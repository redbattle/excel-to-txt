# coding=utf-8
import xlwings as xw

import os

area = '华美璟苑' # 小区名称

path = './files/' + area #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
s = []
for file in files: #遍历文件夹
    if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        if '.DS_Store' == file:
             continue

        unit_id = input(file + '，输入单元id：')

        wb = xw.Book(r'./files/' + area + '/' + file) # 把需要转成txt的原表格文件放到files文件夹下
        sht = wb.sheets[0]
        list_value = wb.sheets[0].range('A2', 'F100').value  # 需要导出的原表格文件内容范围；参数 range(表格起始位置，F100表格截止位置)
        sht.range('A1:G1').options().value = ['id', 'code', 'unit_id', 'floor', 'type', 'toward', 'area']

        for i in range(len(list_value)):
            if list_value[i][0] == None :
                continue
            list0 = list_value[i][0].split('#')
            print(list0)
            # 第1列 id
            sht.range('A' + str(i+2)).options().value = str(unit_id + str(list0[1]))
            # 第2列 code
            sht.range('B' + str(i+2)).options().value = str(list0[1])
            # 第3列 unit_id
            sht.range('C' + str(i+2)).options().value = unit_id
            # 第4列 floor
            sht.range('D' + str(i+2)).options().value = str(list_value[i][2])
            # 第5列 type
            sht.range('E' + str(i+2)).options().value = str(list_value[i][3])
            # 第6列 toward
            sht.range('F' + str(i+2)).options().value = str(list_value[i][4])
            # 第7列 area
            sht.range('G' + str(i+2)).options().value = str(list_value[i][5])
        wb.save(r'./files/改-' + file)


# wb.close()