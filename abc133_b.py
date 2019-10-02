import itertools

n, d = map(int, input().split())
xs = [list(map(int, input().split())) for _ in range(n)]
sq_num = set([i**2 for i in range(128)])

cnt = 0
for x1, x2 in itertools.combinations(xs, 2):
    distance_sq = sum(map(lambda xx: (xx[0]-xx[1])**2, zip(x1, x2)))
    if distance_sq in sq_num:
        cnt += 1
print(cnt)
