n = int(input())
p = list(map(int, input().split()))
cnt = 0
for p1, p2, p3 in zip(p, p[1:], p[2:]):
    if p2 != max(p1, p2, p3) and p2 != min(p1, p2, p3):
        cnt += 1
print(cnt)
