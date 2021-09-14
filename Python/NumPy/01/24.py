def fact(n):
    if n == 1:
        return 1
    else:
        f = 1
        i = 2
        while (i <= n):
            f = f * i
            i = i + 1
        return f


num = eval(input('请输入一个整数：'))
print(fact(abs(int(num))))
