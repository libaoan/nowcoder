# -*- encoding:utf-8 -*-

"""
HJ67 24点游戏算法

描述

给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,本题对数字选取顺序无要求，但每个数字仅允许使用一次，且不考虑括号运算
此题允许数字重复，如3 3 4 4为合法输入，但是每个数字只允许使用一次，如此处一共有两个3，则运算过程中两个3都被选取计算一次，所以3被调用运算两次，但是对应读入的两个数字
输入描述：

本题有多组案例。对于每组案例读入一个[1,10]的整数，数字允许重复，测试用例保证无异常数字。
输出描述：

对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false
示例1

7 2 1 10

true

"""


def judge(nums, sign):
    s = []
    i = 0
    for _ in range(len(sign)):
        s.append(nums[i])
        s.append(sign[i])
        i = i + 1
    s.append(nums[i])
    return eval("".join(s)) == 24


def srange(nums):
    ss = "+-*/"
    for i in range(len(ss)):
        for j in range(len(ss)):
            for k in range(len(ss)):
                sign = [ss[i], ss[j], ss[k]]
                if judge(nums, sign):
                    print(nums, sign)
                    return True
    return False


def nrange(nums):

    for i in range(len(nums)):
        snum = [nums[i], nums[(i+1)%4], nums[(i+2)%4], nums[(i+3)%4]]
        if srange(snum):
            return "true"
    return "false"



def check(arr, res):

    if res < 1:
        return False

    if len(arr) == 1:
        return arr[0] == res

    for i in range(len(arr)):
        left = arr[:i] + arr[i+1:]
        v = arr[i]
        if check(left, res+v) or check(left, res-v) or check(left, res*v) or check(left, res/v):
            return True
    return False


if __name__ == "__main__":
    while True:
        try:
            #nums = input()
            #nums = map(int, [n.strip() for n in nums.split()])
            nums = [1, 2, 10, 2]
            # nums = ["3", "3", "4", "4"]
            print(check(nums, 24))
        except Exception as e:
            print(e)
            # break