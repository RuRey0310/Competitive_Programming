import math

n,d=map(int,input().split())

ans = n/(1+(d*2))

print(math.ceil(ans))
