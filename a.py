


import sys


def getSort(hs, ws):

    dh = {}
    dw = {}
    for i, h in enumerate(hs):
        dh[i+1] = h
    for i, w in enumerate(ws):
        dw[i+1] = w


    res = []

    for h in sorted(list(set(dh.values()))):
        res2 = []
        for k, v in dh.items():
            if h == v:
                res2.append(k)
        res.append(res2)

    res3 = []
    for ks in res:
        res4 = []
        wss = [dw[k] for k in ks]
        list(set(wss)).sort()
        for w in wss:
            for k in ks:
                if dw[k] == w:
                    res4.append(k)


    res4 = []

    res4 = []
    for k in res3:
        res4.append(str(dh[k]))
    return " ".join(res4)



print getSort([95,96,97,98,99,101,102,103,104, 105], 100)

