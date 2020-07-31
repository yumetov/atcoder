import math
a, b = map(int, input().split())
print(math.ceil(1 + (b - a) / (a - 1)))
