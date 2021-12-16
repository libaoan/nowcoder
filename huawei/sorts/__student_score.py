# -*- encoding:utf-8 -*-

"""
描述

查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
例示：
jack      70
peter     96
Tom       70
smith     67
从高到低  成绩
peter     96
jack      70
Tom       70
smith     67
从低到高
smith     67
jack      70
Tom       70
peter     96

注：0代表从高到低，1代表从低到高

注意：本题含有多组输入数据！
数据范围：人数：，数据组数：
进阶：时间复杂度：，空间复杂度：
输入描述：

输入多行，先输入要排序的人的个数，然后分别输入他们的名字和成绩，以一个空格隔开
输出描述：

按照指定方式输出名字和成绩，名字和成绩之间以一个空格隔开
示例1

输入：
3
0
fang 90
yang 50
ning 70
复制
输出：
fang 90
ning 70
yang 50
复制
示例2

输入：
3
1
fang 90
yang 50
ning 70
3
0
moolgouua 43
aebjag 87
b 67
复制
输出：
yang 50
ning 70
fang 90
aebjag 87
b 67
moolgouua 43
复制
说明：
第一组用例:
3
1
fang 90
yang 50
ning 70
升序排序为：
yang 50
ning 70
fang 90
第二组降序为:
aebjag 87
b 67
moolgouua 43
"""


def merge(nums1, nums2, reverse=False):
    res = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i][1] >= nums2[j][1]:
            res.append(nums1[i])
            i = i + 1
        else:
            res.append(nums2[j])
            j = j + 1
    while i < len(nums1):
        res.append(nums1[i])
        i = i + 1

    while j < len(nums2):
        res.append(nums2[j])
        j = j + 1

    if reverse:
        return res[::-1]
    return res


def sorts(nums, reverse=False):
    ln = len(nums)
    if ln == 1:
        return nums
    i = int(ln / 2)
    nums1 = sorts(nums[:i], reverse)
    nums2 = sorts(nums[i:], reverse)
    return merge(nums1, nums2, reverse=reverse)


def run():
    while True:
        try:
            n = int(input().strip())
            flag = int(input().strip())
            nums = []
            for i in range(n):
                s = input().split()
                nums.append((s[0], int(s[1].strip())))
            if flag == 0:
                res = sorts(nums, reverse=False)
            else:
                res = sorts(nums, reverse=True)
            for r in res:
                print(r[0], r[1])
        except Exception as e:
            # print(e)
            break

def run2():
    nums = [
        ("moolgouua",43),
        ("aebjag", 87),
        ("b", 67)
    ]
    res = sorts(nums)
    for r in res:
        print(r[0], r[1])

run2()