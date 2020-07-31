a, b, c = map(int, input().split())
remaining = c - (a - b)
remaining = max(0, remaining)
print(remaining)
