s = input()
for i, si in enumerate(s):
    if i % 2 == 0 and si not in ('R', 'U', 'D'):
        print('No')
        break
    elif i % 2 == 1 and si not in ('L', 'U', 'D'):
        print('No')
        break
else:
    print('Yes')
