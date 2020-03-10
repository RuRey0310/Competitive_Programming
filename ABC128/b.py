n = int(input())

s = [input().split() for i in range(n)]
# 整数に戻す
for i in range(n):
    s[i][1] = int(s[i][1])

c = s.copy()
s.sort()
s.append("fin")

cnt = 0
for i in range(n):
    if (s[i][0] != s[i + 1][0]):
        for j in reversed(range(i - cnt, i + 1)):
            for k in range(n):
                if s[j][1] == c[k][1]:
                    print(k + 1)
                    break
        cnt = 0
    else:
        cnt += 1
