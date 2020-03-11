n = int(input())
s = [input() for i in range(n)]

dic = {}
for i in range(n):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1

max_dic = max(dic.values())
ans = [i for i, j in dic.items() if j == max_dic]
ans.sort()

for i in range(len(ans)):
    print(ans[i])
