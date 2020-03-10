s = list(map(int, input()))

ans = 753
for i in range(len(s) - 2):
    sum = (s[i] * 100) + (s[i + 1] * 10) + (s[i + 2])
    ans = min(ans, abs(753 - sum))
print(ans)
