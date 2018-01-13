#! /usr/bin/env python
#-*- coding:utf-8 -*-

# 从配置文件中获取单元格地址

# 输出 row col 的形式

import ConfigParser
import sys
import argparse

def main():
	'主函数入口'

	# 解析参数
	parser = argparse.ArgumentParser()
	parser.add_argument("name")
	params = vars(parser.parse_args())
	section = params["name"]

	ini = sys.path[0] + "/" + "address.ini"
	conf = ConfigParser.ConfigParser()
	conf.read(ini)

	# 获取 row
	try:
		row = conf.get(section, "row")
	except Exception as e:
		row = 0
	# 获取 col
	try:
		col = conf.get(section,"col")
	except Exception as e:
		col = 0
	
	print "%d %d"%(int(row),int(col))

if __name__ == "__main__":
	main()