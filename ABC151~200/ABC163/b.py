n, m = map(int, input().split())
a = list(map(int, input().split()))
sub = sum(a)
if sub > n:
    print("-1")
else:
    print(n - sub)