# -*- encoding:utf-8 -*-

"""
HJ107 求解立方根
描述

计算一个浮点数的立方根，不使用库函数。
保留一位小数。

数据范围：
输入描述：

待求解参数，为double类型（一个实数）
输出描述：

输入参数的立方根。保留一位小数。
示例1

输入：
216
复制
输出：
6.0
复制
示例2

输入：
2.7
复制
输出：
1.4
复制
"""




def power3(n):
    i = 20
    while True:
        r = i*i*i
        if r == n:
            return round(i/1.0, 1)
        if r < n:
            ti = i+1
            if ti*ti*ti > n:
                i = i+0.01
                while i*i*i - n < 0:
                    i = i+0.01
                return round(i, 1)
            else:
                i = i + int(i/2)
        if r > n:
            ti = i-1
            if ti*ti*ti < n:
                i = i-0.01
                while i*i*i - n > 0:
                    i = i-0.01
                return round(i, 1)
            else:
                i = int(i/2)

if __name__ == "__main__":
    while True:
        try:
            n = float(input().strip())
            # n = int(n) if int(n) > 1 else float(n)
            if n < 0:
                print("-{:0.1f}".format(power3(-n)))
            else:
                print("{:0.1f}".format(power3(n)))
        except Exception:
            # print(e)
            break