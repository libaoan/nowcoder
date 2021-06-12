# -*- encoding:utf-8 -*-

def isSu(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for i in xrange(2, n/2+1):
        if n%i == 0:
            return False
    return True

def getMax(result):

    max = 0
    for res in result:
        count = len(res)
        if max < count:
            max = count
    return max

def getSets(li):

    if len(li) < 2:
        return []
    if len(li) == 2:
        if isSu(li[0]+li[1]):
            return [[(li[0], li[1])]]
        else:
            return []

    take = li[0]
    r = []
    for i, n in enumerate(li[1:]):
        if i == 0:
            lis = li[2:]
        elif i == len(li[1:])-1:
            lis = li[1:-1]
        else:
            lis = li[1:i+1]+li[i+2:]
        result = getSets(lis)
        if result:
            if isSu(take+n):
                for res in result:
                    res.append((take, n))
                    r.append(res)
            else:
                for res in result:
                    # res.append((take, n))
                    r.append(res)
        else:
            if isSu(take+n):
                r.append([(take, n)])

    return r



li = [2,5,6,13]
li = "9360 2272 15078 15571 4734 18667 10392 17796 12207 14591 8380 10126 11627 1288 24523 568 15754 8400 11280 20964 15482 28433 26109 11147 9628 12296 8500 21628 22561 5532 8830 13253 3231 15580 27278 4824 19217 16038 10091 21071 19587 10243 8786 15529 23644 13228 21503 22706 13546 2937 24488 19924 16138 13815 22460 4122 26823 2987 25011 25469 27224 16237".split()
li = map(int, li)
result = getSets(li)
# result = getSets([3,6])
max = getMax(result)
print result
print max