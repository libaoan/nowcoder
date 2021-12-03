# -*- encoding:utf-8 -*-

"""
描述

蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11

请注意本题含有多组样例输入。

输入描述：

输入正整数N（N不大于100）
输出描述：

输出一个N行的蛇形矩阵。
示例1

输入：
4
复制
输出：
1 3 6 10
2 5 9
4 8
7

"""


def get_matrix(n):

    matrix = []
    for i in range(0, n):
        sub = []
        if i == 0:
            sub.append(1)
        else:
            sub.append(matrix[i-1][0]+i)
        for j in range(1, n-i):
            sub.append(sub[j-1]+j+i+1)
        matrix.append(sub)

    return matrix

if __name__ == "__main__":
    mn = get_matrix(6)
    for m in mn:
        print " ".join([str(n) for n in m])