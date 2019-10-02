n, k = map(int, input().split())
h = map(int, input().split())
n_can_ride = sum(1 for hi in h if k <= hi)
print(n_can_ride)
