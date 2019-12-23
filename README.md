# excel-to-txt
- 安装 `python3` [教程地址](https://www.runoob.com/python3/python3-install.html)
- 【win】安装 `git` [教程地址](https://www.runoob.com/git/git-install-setup.html)
- 【win】鼠标右键用`git`打开`bash`窗口
- 安装依赖库，在项目根目录`excel-to-txt/`下执行
    ```bash
    pip3 install -r requirements.txt
    ```
- 根据需要修改`main.py`文件
    ```bash
    content_first = '9135'  # 商家固定值开头 9135
    content_last = '100224'  # 商家固定值结尾 100224
    business_no = 'TJMP1F101'  # 商铺号 TJMP1F101
    wb = app.books.open(r'./files/20191218145136.xlsx') # 把需要转成txt的原表格文件放到files文件夹下
    list_value = wb.sheets[0].range('A6', 'F100').value  # 需要导出的原表格文件内容范围；参数 range(表格起始位置，表格截止位置)
    ```
- 导出数据，在项目根目录`excel-to-txt/`下执行
    ```bash
    ./run.sh
    ```

