#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#
# @name:    Wascan - Web Application Scanner
# @repo:    https://github.com/m4ll0k/Wascan
# @author:  Momo Outaadi (M4ll0k)
# @license: See the file 'LICENSE.txt

from re import search,I 

def teros(headers,content):
	_ = False
	_ |= search(r'st8\(id|_wat|_wlf\)',str(headers.values()),I) is not None
	if _ : 
		return "Teros/Citrix Application Firewall Enterprise (Teros/Citrix Systems)"