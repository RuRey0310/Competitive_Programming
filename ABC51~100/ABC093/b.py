a, b, k = map(int, input().split())

ans = []
for i in range(a, min(b, a + k)):
    if i in ans:
        continue
    else:
        ans.append(i)
for i in range(max(a, b - k + 1), b + 1):
    if i in ans:
        continue
    else:
        ans.append(i)

for i in range(len(ans)):
    print(ans[i])