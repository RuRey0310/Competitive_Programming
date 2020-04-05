abc = list(map(int, input().split()))

abc.sort()
ans = 0

while True:
    if abc[0] == abc[1] and abc[1] == abc[2]:
        print(ans)
        break

    if abc[1] != abc[2]:
        abc[0] += 1
        abc[1] += 1
        ans += 1
    elif abc[1] == abc[2] and abc[1] + 1 == abc[0]:
        abc[1] += 1
        abc[2] += 1
        ans += 1
    else:
        abc[0] += 2
        ans += 1
    