n_s = input()
n = int(n_s)
ans = 0
for i in range(1, len(n_s)):
    if i % 2 == 1:
        ans += 10**i - 10 ** (i-1)
if len(n_s) % 2 == 1:
    ans += 1 + n - 10 ** (len(n_s) - 1)
print(ans)
