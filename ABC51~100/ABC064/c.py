from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    if a[i] >= 3200:
        d["free"] += 1
    elif a[i] >= 2800:
        d["red"] += 1
    elif a[i] >= 2400:
        d["ora"] += 1
    elif a[i] >= 2000:
        d["yellow"] += 1
    elif a[i] >= 1600:
        d["blue"] += 1
    elif a[i] >= 1200:
        d["rblue"] += 1
    elif a[i] >= 800:
        d["green"] += 1
    elif a[i] >= 400:
        d["brown"] += 1
    else:
        d["gray"] += 1

ans = 0
fr = 0
for i in d:
    if i == "free":
        fr += d[i]
    else:
        ans += 1

print(max(ans,1),ans+fr)