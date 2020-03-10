n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

highmax = 0
maxs=0
for i in range(n):
    if highmax < a[i]:
        highmax = a[i]
        maxs = i

for i in range(n):
    max = 0
    if maxs != i:
        print(a[maxs])
    else:
        for j in range(n):
            if i != j:
                if max < a[j]:
                    max = a[j]
        print(max)
            
