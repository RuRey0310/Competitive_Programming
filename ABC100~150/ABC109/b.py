n = int(input())
w = list(input() for i in range(n))

back = w[0][-1]

for i in range(n):
    for j in range(i+1,n):
        if w[i] == w[j]:
            print("No")
            exit()

for i in range(1, n):
    pre = w[i][0]
    if pre != back:
        break
    back = w[i][-1]
    if i == n-1:
        print("Yes")
        exit()

print("No")
