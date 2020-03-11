n = int(input())
x = [0]*n
u = [0]*n
for i in range(n):
    x[i],u[i] = map(str,input().split())

sum = 0
for i in range(n):
    if u[i] == "JPY":
        sum+=int(x[i])
    else:
        sum+=380000.0*float(x[i])

print(sum)
