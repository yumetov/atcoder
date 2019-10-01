s = input()
t = input()
nhits = sum(1 for si, ti in zip(s, t) if si == ti)
print(nhits)
