name = list(input())

ans = name[0]
for i in range(len(name)):
    if name[i] == " ":
        ans += name[i + 1]

ans += "RADIO"
print(ans)