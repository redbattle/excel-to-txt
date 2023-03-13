# coding=utf-8
import os

# from natsort import natsorted

# path = input('输入文件夹的完整路径：')
# pre = input('输入前缀：')

path = '/Users/zhaiyu/Desktop/未命名文件夹'
name = '/Users/zhaiyu/Desktop/name.txt'

# 获取需要修改名称的文件列表
filelist = os.listdir(path)
filelist.sort()

# 获取新名字
name_txt = open(name,'r')  #打开文件
txt_data = name_txt.readlines() #读取所有行
for i in range(len(txt_data)):
    tmp_list = txt_data[i].rstrip() #按‘，'切分每行的数据
    # tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
    print(tmp_list)
    old=path+'/'+filelist[i]
    new=path+'/'+tmp_list+'.pdf'
    print(old)
    print(new)
    os.rename(old,new)


print(len(filelist))