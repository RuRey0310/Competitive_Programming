a,b,k = map(int,input().split())

ta = max(a - k, 0)
ao = 0
if a - k >= 0:
    ao = b
else:
    ao = max(b - (k - a), 0)
print(ta,ao)
