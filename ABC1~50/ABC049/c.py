s = input()

erdr = ["erase", "eraser", "dream", "dreamer"]

ans = True
i = 0
while i < len(s):
    five = s[i: i + 5]
    six = s[i: i + 6]
    seven = s[i: i + 7]

    if seven in erdr:
        i += 7
    elif six in erdr:
        i += 6
    elif five in erdr:
        i += 5
    else:
        ans = False
        break

if ans:
    print("YES")
else:
    print("NO")