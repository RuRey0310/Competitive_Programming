a, r, n = map(int, input().split())
mod = 10 ** 9

if a == 1 and r == 1:
    print(1)
elif r == 1:
    print(a)
else:
    sub = a
    cnt = 0
    while (mod >= sub):
        cnt += 1
        if cnt == n:
            break
        sub *= r

    if sub > mod:
        print("large")
    else:
        print(sub)