n, k = map(int, input().split())
s = input()

ans = 0
for i in range(k, n + 1):
    sub = s[i - k :i]
    ans = max(ans, int(sub))
    
print(ans)