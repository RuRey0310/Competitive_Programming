a, b, n = map(int, input().split())

sub = min(b, n)
if b <= n:
    sub -= 1
ans = (a * sub) // b - (a * (sub // b))
print(ans)