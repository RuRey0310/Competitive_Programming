s, l, r = map(int, input().split())

if s <= r and s >= l:
    print(s)
elif s >= r:
    print(r)
else:
    print(l)