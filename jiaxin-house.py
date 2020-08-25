# coding=utf-8
import xlwings as xw

file = input('输入小区文件的完整路径：')
unit_ids = input('单元id是：')

unit_list1 = unit_ids.split(',')
unit_kv = {}
for unit in unit_list1:
    unit_list2 = unit.split('=')
    unit_kv[unit_list2[0]] = unit_list2[1]

# 旧文件
wb = xw.Book(r''+file) # 把需要转成txt的原表格文件放到files文件夹下

sht = wb.sheets[0]

list_value = wb.sheets[0].range('A2', 'G100').value  # 需要导出的原表格文件内容范围；参数 range(表格起始位置，F100表格截止位置)
# sht.range('A1:G100').api.NumberFormat = '@'
sht.range('A1:G1').options().value = ['id', 'code', 'unit_id', 'floor', 'type', 'toward', 'area']
for i in range(len(list_value)):
    if list_value[i][0] == None :
        continue
    list0 = list_value[i][0].split('#')
    print(list_value[i])
    # 第1列 id
    sht.range('A' + str(i+2)).options().value = "'" + str(unit_kv[str(int(list_value[i][1]))] + str(list0[1]))
    # 第2列 code
    sht.range('B' + str(i+2)).options().value = "'" + str(list0[1])
    # 第3列 unit_id
    sht.range('C' + str(i+2)).options().value = "'" + unit_kv[str(int(list_value[i][1]))]
    # 第4列 floor
    sht.range('D' + str(i+2)).options().value = "'" + str(int(list_value[i][2]))
    # 第5列 type
    sht.range('E' + str(i+2)).options().value = "'" + str(list_value[i][3])
    # 第6列 toward
    sht.range('F' + str(i+2)).options().value = "'" + str(list_value[i][4])
    # 第7列 area
    sht.range('G' + str(i+2)).options().value = "'" + str(list_value[i][5])
wb.save()