matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("原矩阵：", matrix)
print("转置矩阵为：", [[row[i] for row in matrix] for i in range(4)])
