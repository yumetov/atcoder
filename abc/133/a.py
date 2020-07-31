n, a, b = map(int, input().split())
cost_by_train = a * n
cost_by_taxi = b
print(min(cost_by_train, cost_by_taxi))
