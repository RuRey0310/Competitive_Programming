n = int(input())
s = list(input())

ans = 0
for i in range(n - 2):
    if s[i] == "A":
        if s[i + 1] == "B":
            if s[i + 2] == "C":
                ans += 1

print(ans)
