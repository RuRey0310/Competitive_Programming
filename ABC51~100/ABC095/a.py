s = list(input())

ans = 700
for i in range(len(s)):
    if s[i] == "o":
        ans += 100

print(ans)