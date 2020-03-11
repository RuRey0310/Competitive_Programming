h, w = map(int, input().split())
ch, wh = map(int, input().split())

ans = 0
for i in range(h-ch):
    for j in range(w-wh):
            ans += 1
print(ans)
