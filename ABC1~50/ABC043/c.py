n = int(input())
a = list(map(int,input().split()))

avg1 = sum(a) // n
avg2 = (sum(a) // n) + 1
ans1 = 0
ans2 = 0
for i in range(n):
    ans1 += abs(a[i] - avg1) ** 2
    ans2 += abs(a[i] - avg2) ** 2

print(min(ans1,ans2))