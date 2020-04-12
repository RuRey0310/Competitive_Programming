n = int(input())
s = list(input())

r = 0
g = 0
b = 0
for i in range(n):
    if s[i] == "R":
        r += 1
    elif s[i] == "G":
        g += 1
    else:
        b += 1

ans = r * g * b
if ans == 0:
    print("0")
else:
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            sub = j - i
            sub2 = (n - 1) - j
            if sub <= sub2:
                if s[i] != s[j] and s[j] != s[j + sub] and s[i] != s[j + sub]:
                    ans -= 1
    print(ans)