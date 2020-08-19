# coding=utf-8
import xlwings as xw

file = input('输入小区文件的完整路径：')
unit_id = input(file + '单元id是：')

# 旧文件
wb = xw.Book(file) # 把需要转成txt的原表格文件放到files文件夹下

sht = wb.sheets[0]

list_value = wb.sheets[0].range('A2', 'F100').value  # 需要导出的原表格文件内容范围；参数 range(表格起始位置，F100表格截止位置)
sht.range('A1:G1').options().value = ['id', 'code', 'unit_id', 'floor', 'type', 'toward', 'area']
for i in range(len(list_value)):
    if list_value[i][0] == None :
        continue
    list0 = list_value[i][0].split('#')
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
wb.save()