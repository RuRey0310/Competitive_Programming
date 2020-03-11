s = list(input())

zero = 0
one = 0
for i in range(len(s)):
    if s[i] == "0":
        zero += 1
    else:
        one += 1

print(len(s)-(max(zero,one)-min(zero,one)))
