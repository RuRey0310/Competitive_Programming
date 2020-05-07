s = list(input())

ans = []
for i in range(len(s)):
    if s[i] == "0":
        ans.append("0")
    elif s[i] == "1":
        ans.append("1")
    else:
        if len(ans) > 0:
            del ans[len(ans) - 1]

ans = ''.join(ans)
print(ans)