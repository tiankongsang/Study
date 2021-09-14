vec = [2, 4, 6, 8, 10]
print([3 * x for x in vec])
vec = [2, 4, 6, 8, 10]
print([3 * x for x in vec if x > 6])
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print([x * y for x in vec1 for y in vec2 if x * y > 0])
