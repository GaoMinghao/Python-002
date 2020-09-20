# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 6:27 PM
# @Author  : minghao.gao
# @FileName: homework.py
# @Software: PyCharm

# task1
"""
区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.dequ
"""
print("容器序列：list,tuple,dict,collection.deque")
print("扁平序列：str")
print("可变序列：list,dict,collection.deque")
print("不可变序列：str,tuple")

# task2
"""
自定义一个 python 函数，实现 map() 函数的功能。
"""


def self_defiled_map(func, args):
    result = []
    for i in args:
        result.append(func(i))
    return result


# task3
"""
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""
import functools
import time


def timer(func):
    @functools.wraps(func)
    def cal_per(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"runitme:{end - start} s")

    return cal_per
