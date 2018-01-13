#! /usr/bin/env python
#-*- coding:utf-8 -*-

# 剪贴板相关操作

import os

def set(text):
	return os.system("echo "+text+"|pbcopy")