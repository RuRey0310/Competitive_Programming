from collections import defaultdict
s = list(input())

d = defaultdict(int)
for i in s:
    d[i] += 1

for i in d:
    if d[i] > 1:
        print("no")
        exit()

print("yes")