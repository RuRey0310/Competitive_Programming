o = list(input())
e = list(input())

for i in range(len(o)):
    print(o[i], end="")
    if i < len(e):
        print(e[i],end="")