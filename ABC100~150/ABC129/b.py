n = int(input())
w = list(map(int,input().split()))

min = 100

for i in range(n-1):
    jsum = 0
    ksum = 0
    for j in range(0,i+1):
        jsum += w[j]
    for k in range(i+1,n):
        ksum += w[k]
    if(abs(jsum-ksum) < min):
        min = abs(jsum-ksum)

print(min)
