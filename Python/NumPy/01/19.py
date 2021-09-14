import random

total = []
for i in range(30):
    total.append(random.randint(1, 150))
print("列表：", total)
sum = 0
for item in total:
    sum = sum + item
total_m = sum + item
total_m = sum // len(total)
print("新列表：", [x - total_m for x in total])
