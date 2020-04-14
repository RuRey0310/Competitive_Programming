import heapq
n, k = map(int, input().split())
ab = [list(map(int,input().split())) for i in range(n)]

heapq.heapify(ab)
ans = 0
for i in range(k):
    sub = heapq.heappop(ab)
    ans += sub[0]
    sub[0] += sub[1]
    heapq.heappush(ab, sub)

print(ans)