n = int(input())
d = list(map(int,input().split()))

d.sort()

left = int((len(d)/2)-1)
right = int(len(d)/2)

cnt = 0
for i in range(d[left]+1,d[right]+1):
    cnt += 1

print(cnt)
