n = int(input())
s = list(map(str, input().split()))

ans = []
for i in range(n):
    if not s[i] in ans:
        ans.append(s[i])
    
if len(ans) == 3:
    print("Three")
else:
    print("Four")