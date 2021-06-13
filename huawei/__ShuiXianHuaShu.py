# -*- encoding:utf-8 -*-

"""
计算3~7位整数里所包含的水仙花数
"""

def isShuiXianHua(s, n):
    if len(s) != n:
        return False
    sum = 0
    for i, ss in enumerate(s):
        sum += int(ss)**n
        if sum > int(s):
            return False
    if sum == int(s):
        return True
    else:
        return False

def main():
    n = 6
    if n < 3 or n > 7:
        print -1
    res = []
    for i in xrange(10 ** (n - 1), 10 ** n):
        if isShuiXianHua(str(i), n):
            res.append(i)
    for r in res:
        print r,

if __name__ == "__main__":
    main()