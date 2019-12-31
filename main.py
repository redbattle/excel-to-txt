# coding=utf-8
import xlwings as xw
import time

content_first = '9135'  # 商家固定值开头 9135
content_last = '100224'  # 商家固定值结尾 100224
business_no = 'TJMP1F101'  # 商铺号 TJMP1F101

wb = xw.Book(r'./files/123456.xlsx') # 把需要转成txt的原表格文件放到files文件夹下
list_value = wb.sheets[0].range('A6', 'F300').value  # 需要导出的原表格文件内容范围；参数 range(表格起始位置，F100表格截止位置)

txt_file = './files/' + business_no + '_' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '_LIST.txt'  # 需要生成的txt文件，生成在files文件夹下
f = open(txt_file, 'w')
for i in range(len(list_value)):
    if list_value[i][0] == None :
        continue
    # 第1列
    f.write(content_first)
    f.write(',')
    # 第2列
    f.write(str(int(list_value[i][0])))
    f.write(',')
    # 第3列
    f.write(str(list_value[i][1]))
    f.write(',')
    # 第4列
    f.write(str(list_value[i][5]))
    f.write(',')
    # 第5列
    f.write(content_last)
    f.write(',')
    f.write(',')
    f.write(',')
    f.write('\n')
f.close()
wb.close()