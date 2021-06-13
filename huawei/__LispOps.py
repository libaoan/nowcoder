# -*- encoding:utf-8 -*-

"""
计算Lisp语言表达式求值， 非法除0错误返回error
"""

def get_subs(s):
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append("(")
        elif c == ")":
            stack = stack[:-1]
            if len(stack) == 0:
                return i
    raise Exception("format error:%s" %s)

def run(s):
    li = s[1:-1]
    assert li[:3] in ["add", "sub", "mul", "div"], AssertionError("format error:%s" %s)
    op = li[:3]

    ss = li[3:].strip()
    if ss[0] == "(":
        first_end = get_subs(ss)
        first = run(ss[:first_end+1])
        if first == "error":
            return first

        ss = ss[first_end+1:].strip()
        if ss[0] == "(":
            second = run(ss)
            if second == "error":
                return second
        else:
            second = int(ss.strip())

    else:
        index = ss.index(" ")
        first = int(ss[:index])
        ss = ss[index:].strip()
        if ss[0] == "(":
            second = run(ss)
            if second == "error":
                return second
        else:
            second = int(ss.strip())


    if op == "add":
        return first + second
    if op == "sub":
        return first - second
    if op == "mul":
        return first * second
    if op == "div":
        if second == 0:
            return "error"
        else:
            return first/second

    raise Exception("format error:%s" %s)



def main():
    s = [
        "(div 12 (sub 45 45))",
        "(add 1 (div -7 3))",
        "(add 1 (add -7 3))"
    ]
    for ss in s:
        print ss, run(ss)

if __name__ == "__main__":
    main()