n = int(input())
ab = [0] * 100
for i in range(1, n + 1):
    s = str(i)
    front = s[0]
    back = s[-1]
    ab[int(front + back)] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += ab[i * 10 + j] * ab[j * 10 + i]

print(ans)
