# -*- encoding:utf-8 -*-

"""
HJ82 将真分数分解为埃及分数

描述

分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
如有多个解，请输出任意一个。
请注意本题含有多组样例输入！


输入描述：

输入一个真分数，String型
输出描述：

输出分解后的string
示例1

输入：
8/11
2/4
复制
输出：
1/2+1/5+1/55+1/110
1/3+1/6
复制
说明：
第二个样例直接输出1/2也是可以的
"""

def trans(n ,m):

    if n == 1:
        return [n ,m]

    res = []

    i = 2
    while True:
        if n/ m - 1 / i == 0:
            res.append(i)
            break
        if n / m - 1 / i > 0:
            res.append(i)
            n = n * i - m
            m = m * i
        i = i + 1
    return res


if __name__ == "__main__":
    while True:
        try:
            nums = input().strip().split("/")
            res = trans(int(nums[0]), int(nums[1]))
            s = ""
            for i in range(len(res)):
                if i == len(res) - 1:
                    s += "1/{}".format(res[i])
                else:
                    s += "1/{}+".format(res[i])
            print(s)
        except Exception as e:
            print(e)
            break
# failed
# 43/77
# 17/73