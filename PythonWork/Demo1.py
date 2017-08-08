#!/usr/bin/eny python
#-*- coding:utf-8 -*-

import sys
import getpass 

pwd = getpass.getpass("Password:")

print(pwd)
print(sys.argv)

n1  = 255
n2 = 1000
print(hex(n1), hex(n2))