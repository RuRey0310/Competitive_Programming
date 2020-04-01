import collections
n = int(input())
s = list(input())

ans = 0
for i in range(1, n):
    TF = [False] * 26
    x = s[0:i]
    y = s[i:]
    col = collections.Counter(x)
    sub = 0
    for one in y:
        if TF[ord(one) - 97] == False:
            if one in col:
                sub += 1
                TF[ord(one) - 97] = True
    ans = max(ans, sub)

print(ans)