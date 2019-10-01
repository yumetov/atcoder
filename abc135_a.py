a, b = map(int, input().split())
ab = a + b
if ab % 2 == 0:
    print(ab//2)
else:
    print('IMPOSSIBLE')
