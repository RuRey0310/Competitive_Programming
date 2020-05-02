import itertools
n, m, q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(q)]

ans = 0
for i in itertools.combinations_with_replacement(range(1, m + 1), n):
    sub = 0
    print(i)
    for j in range(q):
        if i[ab[j][1] - 1] - i[ab[j][0] - 1] == ab[j][2]:
            sub += ab[j][3]
    
    ans = max(sub, ans)

print(ans)