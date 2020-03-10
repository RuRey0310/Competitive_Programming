n, k = map(int, input().split())

if k % 2 == 1:
    ans = pow(n // k, 3)
    print(ans)
else:
    ans1 = pow(n // k, 3)
    ans2 = 0
    for i in range(1, n + 1):
        if i % k == k / 2:
            ans2 += 1
    print(ans1 + pow(ans2, 3))
