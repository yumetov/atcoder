k, x = map(int, input().split())
min_i = x - k + 1
max_i = x + k - 1
min_i = max(min_i, -1000000)
max_i = min(max_i,  1000000)
print(*range(min_i, max_i+1))
