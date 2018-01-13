# read-cell
获取指定Excel单元格值，并自动copy到系统剪贴板，目前只支持MacOS

# 使用说明
## 运行环境
读取Excel依赖[xlrd](https://github.com/python-excel/xlrd)包，所以先要安装依赖

```
sudo pip install xlrd
```

## 参数
```
read-cell.py [-h] -file FILE [-sheet SHEET] -r ROW -c COLUMN
```

- `h` 获取帮助
- `file` 要读取到Excel文件
- `sheet` 要读取到Excel文件中的第几个sheet，索引从0开始，默认为0
- `r` 读取的行号，索引从0开始
- `c` 读取的列号，索引从0开始

## 其他
`address.py`通过传入`name`参数读取同目录下的`address.ini`文件来获取`row col`形式的单元格地址，用于shell自动化

