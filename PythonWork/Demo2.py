#!/usr/bin/env python
#-*- coding:utf-8 -*-

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

result = calc(1, 2, 3, 4)
print(result)
nums = [1, 2, 3, 4]
result = calc(*nums)
print(result)
