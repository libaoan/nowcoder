# -*- encoding:utf-8 -*-
"""
已空格分隔的字符串短句。过滤该字符串，对于正常单词进行逆转（对于包含非字符的单词不进行逆转），
对处理过的字符串，计算X[ouiea][!ouiear]e的个数
"""
def getTarget(li):
    res = []
    for s in li:
        ss = filter(lambda c: ord(c) in range(ord('a'), ord('z')+1) or ord(c) in range(ord('A'), ord('Z')+1), s)
        if len(s) == len(ss):
            ss = s[::-1]
            res.append(ss)
        else:
            res.append(ss)

    count = 0
    for s in res:
        print s,
        for i, _ in enumerate(s):
            if len(s[i:]) >=4 and s[i] not in "aieou" and s[i+1] in "aieou" and s[i+2] not in "aieour" and s[i+3] == "e":
                count += 1
    return count




def main():
    s = ["!ekam a ekekac", "ededir a ekab"]
    for ss in s:
        count = getTarget(ss.strip().split())
        print count


if __name__ == "__main__":
    main()