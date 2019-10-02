n = int(input())
p = map(int, input().split())
n_miss = sum(1 for i1, i2 in zip(range(1, n+1), p) if i1 != i2)
if n_miss in (0, 2):
    print('YES')
else:
    print('NO')
