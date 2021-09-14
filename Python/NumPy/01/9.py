x = [1, 2, 3, 4, 8, 7, 22, 33, 88]
print("原数据：", x)
for i in range(len(x)):
    if (x[i] % 2) != 0:
        x[i] = x[i] * x[i]
        print("处理后：", x)
