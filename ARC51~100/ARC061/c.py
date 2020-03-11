s = list(input())

leng = len(s) - 1
ans = 0
for i in range(2 ** leng):
    bit = []
    for j in range(leng):
        if ((i >> j) & 1):
            bit.append(s[j])
            bit.append("+")
        else:
            bit.append(s[j])
    bit.append(s[leng])
    sub = 0
    plus = 0
    for k in range(len(bit)):
        if bit[k] == "+":
            sub += plus
            plus = 0
        else:
            if plus == 0:
                plus = int(bit[k])
            else:
                plus *= 10
                plus += int(bit[k])
    sub += plus
    ans += sub

print(ans)
