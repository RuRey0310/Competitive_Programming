s = list(input())
n = int(input())
lr = [list(map(int, list(input().split()))) for i in range(n)]

ss = [-1] * len(s)
for i in range(n):
    if ss[lr[i][0] - 1] != -1:
        ss[lr[i][0] - 1] = [ss[lr[i][0] - 1], i]
    else:
        ss[lr[i][0] - 1] = i
    if ss[lr[i][1] - 1] != -1:
        ss[lr[i][1] - 1] = [ss[lr[i][1] - 1], i]
    else:
        ss[lr[i][1] - 1] = i

bo = [False] * len(s)
a = []
for i in range(len(s)):
    if len(a) != 0 and ss[i] == -1:
        bo[i] = True
    elif len(a) != 0 and ss[i] in a:
        a.remove(ss[i])
        bo[i] = True
    elif ss[i] != -1:
        a.append(ss[i])
        bo[i] = True

st = -1
go = -1
ans = []
for i in range(len(s)):
    if st == -1 and bo[i] == True:
        st = i
        continue
    if st != -1 and bo[i] != True:
        go = i - 1
        sub = s[st: go + 1]
        sub.sort()
        ans += sub
        ans += s[i]
        st = -1
        go = -1
        continue
    if st == -1 and bo[i] == False:
        ans.append(s[i])
    if st != -1 and bo[i] == True and i == (len(s) - 1):
        go = i
        sub = s[st: go + 1]
        sub.sort()
        ans += sub

ans = ''.join(ans)
print(ans)