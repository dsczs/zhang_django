def t(n):
    return n * n


flag = 1
while flag:
    num = int(input('请输入一个数字：'))
    print("result is " + str(t(num)))
    if t(num) >= 50:
        pass
    else:
        flag = 0
