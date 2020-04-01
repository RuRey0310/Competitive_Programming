n = int(input())
s = list(input())

#E(東)を向いてる人数
ruiseki = [0]
for i in range(n):
    if s[i] == "E":
        ruiseki.append(ruiseki[i] + 1)
    else:
        ruiseki.append(ruiseki[i])

INF = float("inf")
ans = INF
for i in range(n):
    if s[i] == "E":
        sub = -1
    else:
        sub = 0
    change = i - (ruiseki[i] - ruiseki[0] - sub)
    change += ruiseki[-1] - ruiseki[i]
    ans = min(ans, change)

print(ans)