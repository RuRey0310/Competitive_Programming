n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

buster=0
for i in range(n):
    buster += min(a[i],b[i])
    buster += min(a[i+1],b[i]-min(a[i],b[i]))
    a[i+1] = a[i+1] - (b[i]-min(a[i],b[i]))
    if(a[i+1] < 0): a[i+1] = 0

print(buster)
