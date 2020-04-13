n = int(input())
a = list(map(int, input().split()))

sub = (10 ** 9) + 1
for i in range(n):
    ans = 0
    while a[i] % 2 == 0 and a[i] != 0:
        a[i] = a[i] // 2
        ans += 1
    sub = min(ans, sub)
    
print(sub)