n = int(input())
a = map(int, input().split())
ans = 1 / sum(map(lambda x: 1/x, a))
print(ans)
