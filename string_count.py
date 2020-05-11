# -*- encoding:utf-8 -*-

"""
时间限制：C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：550498
时间限制：C/C++ 1秒，其他语言2秒 空间限制：C/C++ 32M，其他语言64M 热度指数：550498

示例1
输入
复制
ABCDEF
A
输出
复制
1
"""

def test1():
    s = input()
    c = input()

    count = 0
    for i in range(len(s)):
        if s[i].lower() == c.lower():
            count += 1
    print(count)

def test2():
    s = input()
    c = input()

    print(s.lower().count(c.lower()))