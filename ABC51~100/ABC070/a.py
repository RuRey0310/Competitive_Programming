n = list(input())

for i in range(len(n)):
    if n[i] != n[len(n) - 1 - i]:
        print("No")
        exit()
print("Yes")