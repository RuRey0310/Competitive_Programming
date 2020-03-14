n = int(input())

aa = ["a"]
for i in range(1,n):
    sub = []
    for j in range(len(aa)):
        for k in range(i):
            if not aa[j] + chr(97+k) in sub:
                sub.append(aa[j] + chr(97 + k))
    sub.append(aa[len(aa) - 1] + chr(97 + i))
    aa = sub
for i in range(len(aa)):
    print(aa[i])