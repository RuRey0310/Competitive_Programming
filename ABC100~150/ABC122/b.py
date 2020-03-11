s = list(input())

max = 0
for i in range(len(s)):
    for j in reversed(range(len(s) + 1)):
        cnt = 0
        for k in range(i, j):
            if s[k] == "A" or s[k] == "C" or s[k] == "G" or s[k] == "T":
                cnt += 1
            else:
                cnt = 0
                break
        if max < cnt:
            max = cnt
print(max)
