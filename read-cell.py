#! /usr/bin/env python
#-*- coding:utf-8 -*-

# 自动获取xls文件中cell的值

import xlrd
import sys
import os
import argparse
import clipboard

def main():
	'主函数入口'
	# 解析参数
	parser = argparse.ArgumentParser()
	parser.add_argument("-file",help="file name read from",type=str,required=True,dest="file")
	parser.add_argument("-sheet",help="sheet index start on 0， default is 0",type=int,dest="sheet",default=0)
	parser.add_argument("-r",help="row index start on 0",type=int,required=True,dest="row")
	parser.add_argument("-c",help="column index start on 0",type=int,required=True,dest="column")
	params = vars(parser.parse_args())
	#print params
	file = params["file"]
	sheet = params["sheet"]
	row = params["row"]
	column = params["column"]

	# 打开 excel
	wk = xlrd.open_workbook(file)
	
	pw = wk.sheets()[sheet].cell_value(row,column)
	
	# 粘贴到MAC剪贴板
	if clipboard.set(pw) == 0:
		state = "copy ok"
	else:
		state = "copy failed"

	print "%s.[%s%d]: %s\t%s"%(wk.sheet_names()[sheet],chr(params["column"]+65),params["row"]+1,pw,state)



if __name__ == "__main__":
	main()